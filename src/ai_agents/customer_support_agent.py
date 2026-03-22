from typing import Dict, Any
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ai_agents.base_agent import BaseAgent
import config.settings as settings_module

class CustomerSupportAgent(BaseAgent):
    """Agent for handling customer support inquiries"""
    
    def __init__(self):
        super().__init__("customer_support")
        try:
            self.prompts = settings_module.settings.load_prompts()
        except Exception as e:
            print(f"Error loading prompts: {e}")
            self.prompts = {'system_prompts': {'customer_support': 'You are a helpful customer support agent.'}}
        
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate customer inquiry input"""
        return 'message' in input_data
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process customer inquiry and generate response"""
        if not self.validate_input(input_data):
            raise ValueError("Invalid input data: message field required")
        
        # Create context from available data
        context = self._build_context(input_data)
        
        # Get system message
        system_message = self.prompts.get('system_prompts', {}).get('customer_support', 'You are a helpful customer support agent.')
        
        # Generate response using LLM
        response = self.llm_client.generate_response(
            prompt=f"Context: {context}\n\nCustomer question: {input_data['message']}\n\nProvide a helpful response:",
            system_message=system_message
        )
        
        self.log_activity("inquiry_processed", {
            "inquiry_id": input_data.get('inquiry_id'),
            "response_length": len(response)
        })
        
        return {
            "status": "success",
            "reply": response,
            "inquiry_id": input_data.get('inquiry_id'),
            "requires_escalation": self._check_escalation_needed(response)
        }
    
    def _build_context(self, input_data: Dict[str, Any]) -> str:
        """Build context from available data"""
        context_parts = []
        
        if input_data.get('tenant_name'):
            context_parts.append(f"Tenant: {input_data['tenant_name']}")
        if input_data.get('property_id'):
            context_parts.append(f"Property ID: {input_data['property_id']}")
            
        return " | ".join(context_parts) if context_parts else "No additional context available"
    
    def _check_escalation_needed(self, response: str) -> bool:
        """Check if the response requires human escalation"""
        escalation_keywords = ['escalate', 'human agent', 'supervisor', 'cannot resolve', 'talk to a person']
        return any(keyword in response.lower() for keyword in escalation_keywords)