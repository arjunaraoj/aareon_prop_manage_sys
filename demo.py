"""Demo script for Aareon AI Agent System (works without API key)"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

def run_demo():
    """Run a demo of the AI agents"""
    
    print("=" * 60)
    print("Aareon AI Agent System - Demo Mode")
    print("=" * 60)
    
    try:
        # Import agents
        print("\nImporting modules...")
        from src.ai_agents.document_processor_agent import DocumentProcessorAgent
        from src.ai_agents.customer_support_agent import CustomerSupportAgent
        from src.ai_agents.process_automation_agent import ProcessAutomationAgent
        print("✓ Modules imported successfully")
        
        # Initialize agents
        print("\nInitializing AI Agents...")
        doc_agent = DocumentProcessorAgent()
        print("  ✓ Document Processor Agent initialized")
        
        cs_agent = CustomerSupportAgent()
        print("  ✓ Customer Support Agent initialized")
        
        pa_agent = ProcessAutomationAgent()
        print("  ✓ Process Automation Agent initialized")
        
        # Test Document Processing
        print("\n" + "=" * 60)
        print("1. Testing Document Processing Agent")
        print("=" * 60)
        
        test_doc = {
            "document_type": "maintenance_request",
            "content": "Maintenance request for property P1001: Leaking faucet in kitchen. Urgent issue reported by tenant Jan de Vries. Contact: 0612345678",
            "source": "test_input"
        }
        
        result = doc_agent.process(test_doc)
        print(f"\nDocument Type: {result['document_type']}")
        print(f"Status: {result['status']}")
        print(f"Confidence: {result.get('confidence', 0):.2%}")
        print(f"Extracted Info: {result.get('extracted_info', {})}")
        
        # Test Customer Support
        print("\n" + "=" * 60)
        print("2. Testing Customer Support Agent")
        print("=" * 60)
        
        test_inquiry = {
            "inquiry_id": "TEST001",
            "message": "How do I report a maintenance issue?",
            "tenant_name": "Jan de Vries",
            "property_id": "P1001"
        }
        
        response = cs_agent.process(test_inquiry)
        print(f"\nInquiry: {test_inquiry['message']}")
        print(f"Response: {response.get('reply', 'No response')}")
        print(f"Requires Escalation: {response.get('requires_escalation', False)}")
        
        # Test Process Automation
        print("\n" + "=" * 60)
        print("3. Testing Process Automation Agent")
        print("=" * 60)
        
        test_process = {
            "process_type": "maintenance_scheduling",
            "property_id": "P1001",
            "priority": "High"
        }
        
        automation = pa_agent.process(test_process)
        print(f"\nProcess Type: {automation.get('process_type', 'Unknown')}")
        print(f"Status: {automation.get('status', 'Unknown')}")
        print(f"Estimated Time Savings: {automation.get('estimated_time_savings', 'N/A')}")
        
        if 'automation_plan' in automation:
            print("\nAutomation Opportunities:")
            for opp in automation['automation_plan'].get('automation_opportunities', []):
                print(f"  • {opp}")
        
        # Summary
        print("\n" + "=" * 60)
        print("Demo Complete!")
        print("=" * 60)
        
        # Check API key status
        from config.settings import settings
        if not settings.OPENAI_API_KEY:
            print("\n⚠️  Note: This is running in demo mode with mock responses.")
            print("   To enable full AI capabilities:")
            print("   1. Get an OpenAI API key from https://platform.openai.com/api-keys")
            print("   2. Add it to the .env file: OPENAI_API_KEY=your-key-here")
            print("   3. Run the demo again to see actual AI-powered responses")
        else:
            print("\n✓ OpenAI API key detected! Running with actual AI responses.")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print("\nTroubleshooting tips:")
        print("1. Make sure you're in the correct directory")
        print("2. Check that all required files exist")
        print("3. Try running: pip install -r requirements.txt")
        print("4. If you have OpenAI key, add it to .env file")

if __name__ == "__main__":
    run_demo()