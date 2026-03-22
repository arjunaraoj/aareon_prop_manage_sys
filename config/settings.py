import os
from dotenv import load_dotenv
import yaml
from pathlib import Path

# Load environment variables
load_dotenv()

class Settings:
    # OpenAI Settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Azure Settings (optional)
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    
    # Application Settings
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 4096))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Vector Store Settings
    CHROMA_PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./data/chroma_db")
    
    # Data Paths
    DATA_RAW_PATH = "./data/raw"
    DATA_PROCESSED_PATH = "./data/processed"
    
    @classmethod
    def load_prompts(cls):
        """Load prompts from YAML file"""
        # Try to get the config directory path
        current_dir = Path(__file__).parent
        prompt_file = current_dir / "prompts.yaml"
        
        if prompt_file.exists():
            try:
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                print(f"Error loading prompts: {e}")
                return cls._get_default_prompts()
        else:
            print(f"Prompt file not found at {prompt_file}, using defaults")
            return cls._get_default_prompts()
    
    @classmethod
    def _get_default_prompts(cls):
        """Return default prompts if file doesn't exist"""
        return {
            'system_prompts': {
                'document_processor': 'You are an AI document processor for Aareon, specializing in real estate property management documents. Extract key information such as property details, maintenance requests, and tenant information. Be precise and structured in your output.',
                'customer_support': 'You are a customer support AI agent for Aareon, helping tenants and property owners with their inquiries. Be helpful, professional, and empathetic. Focus on resolving issues efficiently.',
                'process_automation': 'You are a process automation AI agent that helps streamline real estate management workflows. Analyze the given tasks and suggest optimal automation strategies.'
            },
            'rag_prompts': {
                'retrieval_instruction': 'Based on the following context from our property management database, answer the question accurately.',
                'context_combination': 'Combine the following pieces of information into a coherent response.'
            }
        }

# Create a singleton instance
settings = Settings()