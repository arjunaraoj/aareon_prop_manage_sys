from typing import Dict, Any
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ai_agents.base_agent import BaseAgent
import config.settings as settings_module

class ProcessAutomationAgent(BaseAgent):
    """Agent for automating business processes"""
    
    def __init__(self):
        super().__init__("process_automation")
        try:
            self.prompts = settings_module.settings.load_prompts()
        except Exception as e:
            print(f"Error loading prompts: {e}")
            self.prompts = {'system_prompts': {'process_automation': 'You are a process automation specialist.'}}
        
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate process automation input"""
        return 'process_type' in input_data
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze and suggest automation for business processes"""
        if not self.validate_input(input_data):
            raise ValueError("Invalid input data: process_type field required")
        
        # Get system message
        system_message = self.prompts.get('system_prompts', {}).get('process_automation', 'You are a process automation specialist.')
        
        # Analyze process and suggest automation
        automation_plan = self._analyze_process(input_data)
        
        # Generate automation workflow
        workflow = self._generate_workflow(automation_plan, input_data)
        
        self.log_activity("process_automated", {
            "process_type": input_data['process_type'],
            "steps": len(workflow.get('steps', []))
        })
        
        return {
            "status": "success",
            "process_type": input_data['process_type'],
            "automation_plan": automation_plan,
            "workflow": workflow,
            "estimated_time_savings": automation_plan.get('time_savings', 'Unknown')
        }
    
    def _analyze_process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze the process for automation opportunities"""
        analysis = {
            "process_type": input_data['process_type'],
            "automation_opportunities": [],
            "complexity": "medium",
            "time_savings": "2-4 hours per week"
        }
        
        if input_data['process_type'] == "maintenance_scheduling":
            analysis['automation_opportunities'] = [
                "Auto-assign technicians based on availability and skills",
                "Send automated notifications to tenants via SMS/Email",
                "Generate work orders automatically",
                "Track completion status in real-time",
                "Automated follow-up after completion"
            ]
            analysis['complexity'] = "medium"
            analysis['time_savings'] = "3-5 hours per week"
            
        elif input_data['process_type'] == "rent_collection":
            analysis['automation_opportunities'] = [
                "Send automatic payment reminders before due date",
                "Process payments automatically via API integration",
                "Generate and send late fee notices",
                "Update payment status in real-time",
                "Generate monthly financial reports"
            ]
            analysis['complexity'] = "high"
            analysis['time_savings'] = "5-8 hours per week"
            
        elif input_data['process_type'] == "document_processing":
            analysis['automation_opportunities'] = [
                "Auto-classify documents by type",
                "Extract key information using AI",
                "Store documents with proper metadata",
                "Route documents to appropriate departments",
                "Generate document summaries"
            ]
            analysis['complexity'] = "medium"
            analysis['time_savings'] = "4-6 hours per week"
            
        else:
            analysis['automation_opportunities'] = [
                "Identify repetitive tasks in the workflow",
                "Create standard operating procedures",
                "Implement workflow automation tools",
                "Set up automated notifications",
                "Track and report metrics"
            ]
            
        return analysis
    
    def _generate_workflow(self, analysis: Dict[str, Any], input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate automation workflow steps"""
        workflow = {
            "steps": [],
            "triggers": [],
            "actions": [],
            "estimated_timeline": "2-4 weeks"
        }
        
        # Add workflow steps based on process type
        for i, opportunity in enumerate(analysis.get('automation_opportunities', []), 1):
            workflow['steps'].append({
                "step_id": i,
                "name": opportunity,
                "status": "proposed",
                "priority": "high" if i <= 2 else "medium",
                "estimated_effort": "2-3 days"
            })
        
        # Add triggers
        workflow['triggers'] = [
            "Manual initiation by staff",
            "Scheduled time-based execution",
            "Event-based triggers (e.g., new document uploaded)"
        ]
        
        # Add actions
        workflow['actions'] = [
            "API calls to external systems",
            "Database updates",
            "Email/SMS notifications",
            "Report generation"
        ]
            
        return workflow