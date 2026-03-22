import openai
from typing import List, Dict, Any, Optional, Generator
import tiktoken
import sys
import os
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from config.settings import settings
from src.utils.logger import setup_logger

class LLMClient:
    """Client for interacting with OpenAI's API"""
    
    def __init__(self):
        self.logger = setup_logger("llm_client", logging.INFO)
        self.model = settings.OPENAI_MODEL
        self.max_tokens = settings.MAX_TOKENS
        self.temperature = settings.TEMPERATURE
        
        # Initialize OpenAI client only if API key is provided
        if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY != "":
            try:
                openai.api_key = settings.OPENAI_API_KEY
                self.is_available = True
                try:
                    self.encoding = tiktoken.encoding_for_model(self.model)
                except:
                    self.encoding = tiktoken.get_encoding("cl100k_base")
                self.logger.info("OpenAI client initialized successfully")
            except Exception as e:
                self.logger.error(f"Failed to initialize OpenAI client: {e}")
                self.is_available = False
        else:
            self.logger.warning("No OpenAI API key found. Running in demo mode with mock responses.")
            self.is_available = False
        
    def generate_response(self, 
                         prompt: str, 
                         system_message: Optional[str] = None,
                         temperature: Optional[float] = None) -> str:
        """Generate a response from the LLM"""
        if not self.is_available:
            # Return mock response for demo/testing
            return self._get_mock_response(prompt)
            
        try:
            messages = []
            if system_message:
                messages.append({"role": "system", "content": system_message})
            messages.append({"role": "user", "content": prompt})
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=temperature or self.temperature,
                max_tokens=self.max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return f"I'm having trouble processing your request. Error: {str(e)}"
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in a text string"""
        if not self.is_available:
            # Rough estimate for demo mode
            return len(text) // 4
        
        try:
            return len(self.encoding.encode(text))
        except:
            return len(text) // 4
    
    def generate_streaming(self, 
                          prompt: str, 
                          system_message: Optional[str] = None) -> Generator[str, None, None]:
        """Generate streaming response"""
        if not self.is_available:
            # Mock streaming response
            mock_response = self._get_mock_response(prompt)
            for chunk in mock_response.split():
                yield chunk + " "
            return
            
        try:
            messages = []
            if system_message:
                messages.append({"role": "system", "content": system_message})
            messages.append({"role": "user", "content": prompt})
            
            stream = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.get("content"):
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            self.logger.error(f"Error in streaming: {e}")
            yield f"Error: {str(e)}"
    
    def _get_mock_response(self, prompt: str) -> str:
        """Generate mock response for demo mode"""
        mock_responses = {
            "maintenance": "Based on the maintenance request, I recommend scheduling a technician to inspect the issue. Please provide the property ID and preferred time for the visit.",
            "lease": "I can help with lease agreements. Please specify if you need to review, renew, or create a new lease agreement.",
            "payment": "For payment-related inquiries, you can make payments through our online portal or contact the accounting department.",
            "document": "I've analyzed the document and extracted the key information. The document appears to be a property management record.",
            "default": "Thank you for your inquiry. Our AI system is currently in demo mode. For production use, please configure your OpenAI API key in the .env file."
        }
        
        # Simple keyword matching for mock responses
        prompt_lower = prompt.lower()
        for keyword, response in mock_responses.items():
            if keyword in prompt_lower:
                return response
        
        return mock_responses["default"]