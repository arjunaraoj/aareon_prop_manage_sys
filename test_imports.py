"""Test script to verify all imports work"""

import sys
import os

print("Testing imports...")
print("=" * 50)

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

# Test settings import
try:
    from config.settings import settings
    print("✓ settings imported successfully")
except Exception as e:
    print(f"✗ settings import failed: {e}")

# Test base agent
try:
    from src.ai_agents.base_agent import BaseAgent
    print("✓ BaseAgent imported successfully")
except Exception as e:
    print(f"✗ BaseAgent import failed: {e}")

# Test document processor
try:
    from src.ai_agents.document_processor_agent import DocumentProcessorAgent
    print("✓ DocumentProcessorAgent imported successfully")
except Exception as e:
    print(f"✗ DocumentProcessorAgent import failed: {e}")

# Test customer support
try:
    from src.ai_agents.customer_support_agent import CustomerSupportAgent
    print("✓ CustomerSupportAgent imported successfully")
except Exception as e:
    print(f"✗ CustomerSupportAgent import failed: {e}")

# Test process automation
try:
    from src.ai_agents.process_automation_agent import ProcessAutomationAgent
    print("✓ ProcessAutomationAgent imported successfully")
except Exception as e:
    print(f"✗ ProcessAutomationAgent import failed: {e}")

# Test core modules
try:
    from src.core.llm_client import LLMClient
    print("✓ LLMClient imported successfully")
except Exception as e:
    print(f"✗ LLMClient import failed: {e}")

# Test rag modules
try:
    from src.rag.document_loader import DocumentLoader
    from src.rag.retriever import Retriever
    print("✓ RAG modules imported successfully")
except Exception as e:
    print(f"✗ RAG modules import failed: {e}")

# Test utils
try:
    from src.utils.logger import setup_logger
    from src.utils.data_processor import DataProcessor
    print("✓ Utils modules imported successfully")
except Exception as e:
    print(f"✗ Utils modules import failed: {e}")

print("=" * 50)
print("Import test complete!")