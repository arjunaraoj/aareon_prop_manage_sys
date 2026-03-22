from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging
import sys
import os

# Add parent directory to path to allow absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.core.llm_client import LLMClient
from src.utils.logger import setup_logger

class BaseAgent(ABC):
    """Base class for all AI agents"""
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.logger = setup_logger(f"{agent_name}_agent", logging.INFO)
        self.llm_client = LLMClient()
        
    @abstractmethod
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input data and return results"""
        pass
    
    @abstractmethod
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate input data before processing"""
        pass
    
    def log_activity(self, action: str, details: Dict[str, Any]) -> None:
        """Log agent activities for monitoring"""
        self.logger.info(f"Agent: {self.agent_name}, Action: {action}, Details: {details}")