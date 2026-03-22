#!/usr/bin/env python
"""Setup script for Aareon AI Agent System"""

import os
import sys
from pathlib import Path

def setup_environment():
    """Setup the project environment"""
    
    # Get project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print(f"Setting up project in: {project_root}")
    
    # Create necessary directories
    directories = [
        "data/raw",
        "data/processed",
        "logs",
        "tests",
        "notebooks"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Check for .env file
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            import shutil
            shutil.copy(".env.example", ".env")
            print("Created .env file from .env.example")
            print("Please edit .env and add your OpenAI API key")
    
    # Install requirements
    print("\nInstalling requirements...")
    os.system(f"{sys.executable} -m pip install -r requirements.txt")
    
    print("\nSetup complete!")
    print("\nNext steps:")
    print("1. Add your OpenAI API key to .env file")
    print("2. Run: python scripts/load_sample_data.py")
    print("3. Run: python -m src.main")

if __name__ == "__main__":
    setup_environment()