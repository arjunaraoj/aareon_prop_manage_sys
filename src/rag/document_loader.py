from typing import List, Dict, Any
import sys
import os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class DocumentLoader:
    """Load documents from various sources"""
    
    def __init__(self):
        pass
        
    def load_csv(self, file_path: str) -> List[Dict[str, Any]]:
        """Load CSV file as documents"""
        df = pd.read_csv(file_path)
        documents = []
        
        for idx, row in df.iterrows():
            documents.append({
                "content": row.to_string(),
                "metadata": {"source": file_path, "row": idx}
            })
            
        return documents