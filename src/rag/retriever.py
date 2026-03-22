from typing import List, Dict, Any
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.core.vector_store import VectorStore

class Retriever:
    """Retrieve relevant documents"""
    
    def __init__(self):
        self.vector_store = VectorStore()
        
    def add_document(self, content: str, metadata: Dict[str, Any]) -> None:
        """Add a document to the retriever"""
        self.vector_store.add_documents([{
            "content": content,
            "metadata": metadata
        }])
        
    def retrieve(self, query: str, k: int = 3) -> List[Dict[str, Any]]:
        """Retrieve relevant documents"""
        return self.vector_store.similarity_search(query, k)