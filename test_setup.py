"""Test script to verify the setup"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

print("Testing imports...")

try:
    from src.utils.logger import setup_logger
    print("✓ Logger imported")
except Exception as e:
    print(f"✗ Logger import failed: {e}")

try:
    from src.core.llm_client import LLMClient
    print("✓ LLMClient imported")
except Exception as e:
    print(f"✗ LLMClient import failed: {e}")

try:
    from src.ai_agents.base_agent import BaseAgent
    print("✓ BaseAgent imported")
except Exception as e:
    print(f"✗ BaseAgent import failed: {e}")

try:
    from config.settings import settings
    print("✓ Settings imported")
    print(f"  OpenAI Model: {settings.OPENAI_MODEL}")
    print(f"  OpenAI API Key set: {'Yes' if settings.OPENAI_API_KEY else 'No'}")
except Exception as e:
    print(f"✗ Settings import failed: {e}")

print("\nSetup test complete!")