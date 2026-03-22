import asyncio
from typing import Dict, Any
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ai_agents.document_processor_agent import DocumentProcessorAgent
from src.ai_agents.customer_support_agent import CustomerSupportAgent
from src.ai_agents.process_automation_agent import ProcessAutomationAgent
from src.utils.logger import setup_logger
import logging

class AareonAISystem:
    """Main AI System for Aareon"""
    
    def __init__(self):
        self.logger = setup_logger("aareon_ai_system", logging.INFO)
        self.document_processor = DocumentProcessorAgent()
        self.customer_support = CustomerSupportAgent()
        self.process_automation = ProcessAutomationAgent()
        
    async def process_document(self, document_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a document through the AI system"""
        try:
            result = self.document_processor.process(document_data)
            self.logger.info(f"Document processed successfully")
            return result
        except Exception as e:
            self.logger.error(f"Error processing document: {e}")
            return {"status": "error", "message": str(e)}
    
    async def handle_customer_inquiry(self, inquiry: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer inquiry through AI"""
        try:
            response = self.customer_support.process(inquiry)
            self.logger.info(f"Customer inquiry handled")
            return response
        except Exception as e:
            self.logger.error(f"Error handling inquiry: {e}")
            return {"status": "error", "message": str(e)}
    
    async def automate_process(self, process_data: Dict[str, Any]) -> Dict[str, Any]:
        """Automate a process using AI"""
        try:
            result = self.process_automation.process(process_data)
            self.logger.info(f"Process automated")
            return result
        except Exception as e:
            self.logger.error(f"Error automating process: {e}")
            return {"status": "error", "message": str(e)}

async def main():
    """Main entry point"""
    # Initialize the AI system
    ai_system = AareonAISystem()
    
    print("=" * 60)
    print("Aareon AI Agent System")
    print("=" * 60)
    
    # Check if OpenAI API is configured
    from config.settings import settings
    if not settings.OPENAI_API_KEY:
        print("\n⚠️  WARNING: No OpenAI API key found!")
        print("   Running in demo mode with mock responses.")
        print("   To enable full AI capabilities, add your API key to .env file\n")
    
    # Example: Process a maintenance request document
    print("\n1. Processing Document...")
    document_data = {
        "document_type": "maintenance_request",
        "content": "Maintenance request for property P1001: Leaking faucet in kitchen. Urgent issue reported by tenant Jan de Vries.",
        "source": "user_input"
    }
    result = await ai_system.process_document(document_data)
    print(f"   Status: {result['status']}")
    print(f"   Extracted Info: {result.get('extracted_info', 'N/A')}")
    
    # Example: Handle customer inquiry
    print("\n2. Handling Customer Inquiry...")
    inquiry = {
        "inquiry_id": "INQ001",
        "message": "How do I report a maintenance issue?",
        "tenant_name": "Jan de Vries",
        "property_id": "P1001"
    }
    response = await ai_system.handle_customer_inquiry(inquiry)
    print(f"   Status: {response['status']}")
    print(f"   Response: {response.get('reply', 'N/A')[:100]}...")
    
    # Example: Automate process
    print("\n3. Automating Process...")
    process_data = {
        "process_type": "maintenance_scheduling",
        "property_id": "P1001",
        "priority": "High"
    }
    automation_result = await ai_system.automate_process(process_data)
    print(f"   Status: {automation_result['status']}")
    print(f"   Process Type: {automation_result.get('process_type', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("System Ready!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())