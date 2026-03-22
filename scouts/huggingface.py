"""
HuggingFace Scout - Discovers models from HuggingFace Hub
"""

import requests
from datetime import datetime, timedelta
from typing import List, Dict

class HuggingFaceScout:
    """Scout for HuggingFace Hub models."""
    
    BASE_URL = "https://huggingface.co/api"
    
    def __init__(self, token: str = None):
        self.token = token
        self.headers = {}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
    
    def get_trending(self, limit: int = 50) -> List[Dict]:
        """Get trending models from HuggingFace."""
        url = f"{self.BASE_URL}/trending?limit={limit}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching trending: {e}")
            return []
    
    def get_new_models(self, since_days: int = 7, limit: int = 100) -> List[Dict]:
        """Get newly created models."""
        since = (datetime.now() - timedelta(days=since_days)).isoformat()
        url = f"{self.BASE_URL}/models?sort=created\u0026limit={limit}\u0026full=true"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            models = response.json()
            # Filter by date
            return [m for m in models if m.get('created_at', '') > since]
        except Exception as e:
            print(f"Error fetching new models: {e}")
            return []
    
    def get_top_downloads(self, limit: int = 100) -> List[Dict]:
        """Get most downloaded models."""
        url = f"{self.BASE_URL}/models?sort=downloads\u0026limit={limit}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching top downloads: {e}")
            return []
    
    def get_model_info(self, model_id: str) -> Dict:
        """Get detailed info about a specific model."""
        url = f"{self.BASE_URL}/models/{model_id}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching model {model_id}: {e}")
            return {}
    
    def check_ollama_compatibility(self, model_info: Dict) -> bool:
        """Check if model is likely Ollama-compatible."""
        tags = model_info.get('tags', [])
        
        # Check for GGUF or safetensors
        has_gguf = any('gguf' in tag.lower() for tag in tags)
        has_safetensors = 'safetensors' in tags
        
        # Check for common architectures
        architectures = model_info.get('config', {}).get('architectures', [])
        supported = ['LlamaForCausalLM', 'GPTNeoXForCausalLM', 'MistralForCausalLM']
        has_supported_arch = any(arch in supported for arch in architectures)
        
        return has_gguf or (has_safetensors and has_supported_arch)
