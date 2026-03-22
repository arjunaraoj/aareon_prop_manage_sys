from typing import Dict, Any, List
import json
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ai_agents.base_agent import BaseAgent
from src.rag.document_loader import DocumentLoader
from src.rag.retriever import Retriever
import config.settings as settings_module

class DocumentProcessorAgent(BaseAgent):
    """Agent for processing documents and extracting information"""
    
    def __init__(self):
        super().__init__("document_processor")
        self.document_loader = DocumentLoader()
        self.retriever = Retriever()
        try:
            self.prompts = settings_module.settings.load_prompts()
        except Exception as e:
            print(f"Error loading prompts: {e}")
            self.prompts = {'system_prompts': {'document_processor': 'You are a document processor.'}}
        
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate document input"""
        required_fields = ['document_type', 'content']
        return all(field in input_data for field in required_fields)
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process document and extract key information"""
        if not self.validate_input(input_data):
            raise ValueError("Invalid input data")
            
        document_type = input_data['document_type']
        content = input_data['content']
        
        # Create extraction prompt
        extraction_prompt = self._create_extraction_prompt(document_type, content)
        
        # Get system message
        system_message = self.prompts.get('system_prompts', {}).get('document_processor', 'You are a document processor.')
        
        # Extract information using LLM
        extracted_info = self.llm_client.generate_response(
            prompt=extraction_prompt,
            system_message=system_message
        )
        
        # Parse and structure the extracted information
        structured_data = self._structure_extracted_data(extracted_info, document_type)
        
        # Store in vector database for retrieval
        try:
            self.retriever.add_document(
                content=json.dumps(structured_data),
                metadata={"type": document_type, "source": input_data.get('source', 'unknown')}
            )
        except Exception as e:
            self.logger.warning(f"Could not store document in retriever: {e}")
        
        self.log_activity("document_processed", {
            "document_type": document_type,
            "extracted_fields": list(structured_data.keys())
        })
        
        return {
            "status": "success",
            "document_type": document_type,
            "extracted_info": structured_data,
            "confidence": self._calculate_confidence(extracted_info)
        }
    
    def _create_extraction_prompt(self, doc_type: str, content: str) -> str:
        """Create extraction prompt based on document type"""
        prompts = {
            "maintenance_request": f"Extract maintenance request details: property ID, issue description, urgency, contact person. Return as JSON. Content: {content}",
            "lease_agreement": f"Extract lease agreement details: tenant name, property address, lease term, monthly rent. Return as JSON. Content: {content}",
            "invoice": f"Extract invoice details: invoice number, amount, due date, vendor. Return as JSON. Content: {content}",
            "property_inspection": f"Extract inspection report details: property ID, inspection date, findings, recommendations. Return as JSON. Content: {content}"
        }
        return prompts.get(doc_type, f"Extract key information from this document and return as JSON: {content}")
    
    def _structure_extracted_data(self, extracted_info: str, doc_type: str) -> Dict:
        """Structure extracted information into a consistent format"""
        try:
            # Try to parse as JSON first
            return json.loads(extracted_info)
        except:
            # If not JSON, create structured dict
            return {
                "type": doc_type,
                "content": extracted_info,
                "extracted_at": pd.Timestamp.now().isoformat()
            }
    
    def _calculate_confidence(self, extracted_info: str) -> float:
        """Calculate confidence score for extraction"""
        # Simple heuristic: longer extracted text might indicate more complete extraction
        return min(1.0, len(extracted_info) / 500)