import pandas as pd
from typing import Dict, Any
import os

class DataProcessor:
    """Process and load data files"""
    
    def __init__(self):
        pass
    
    def load_document(self, file_path: str) -> Dict[str, Any]:
        """Load document from file path"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Determine file type from extension
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.csv':
            df = pd.read_csv(file_path)
            return {
                "content": df.to_string(),
                "type": "csv",
                "rows": len(df),
                "columns": list(df.columns)
            }
        elif ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {
                "content": content,
                "type": "text",
                "size": len(content)
            }
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    
    def save_results(self, data: Any, file_path: str) -> None:
        """Save results to file"""
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        if file_path.endswith('.csv'):
            if isinstance(data, pd.DataFrame):
                data.to_csv(file_path, index=False)
            else:
                pd.DataFrame([data]).to_csv(file_path, index=False)
        elif file_path.endswith('.json'):
            import json
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)