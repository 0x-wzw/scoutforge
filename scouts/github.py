"""
GitHub Crawler - Discovers model repos from GitHub
"""

import requests
from datetime import datetime, timedelta
from typing import List, Dict

class GitHubCrawler:
    """Crawl GitHub for model-related repositories."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: str = None):
        self.token = token
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def search_repos(self, query: str, sort: str = "updated", 
                     order: str = "desc", per_page: int = 100) -> List[Dict]:
        """Search GitHub repositories."""
        url = f"{self.BASE_URL}/search/repositories"
        params = {
            "q": query,
            "sort": sort,
            "order": order,
            "per_page": per_page
        }
        
        try:
            response = requests.get(url, headers=self.headers, 
                                   params=params, timeout=30)
            response.raise_for_status()
            return response.json().get('items', [])
        except Exception as e:
            print(f"Error searching repos: {e}")
            return []
    
    def find_new_gguf_repos(self, since_days: int = 7) -> List[Dict]:
        """Find new repos with GGUF models."""
        since_date = (datetime.now() - timedelta(days=since_days)).strftime("%Y-%m-%d")
        query = f"GGUF OR safetensors created:\u003e{since_date}"
        return self.search_repos(query)
    
    def find_inference_frameworks(self) -> List[Dict]:
        """Find popular inference frameworks."""
        query = "llama.cpp OR llamafile OR ollama stars:\u003e100"
        return self.search_repos(query, sort="stars")
    
    def find_training_tools(self) -> List[Dict]:
        """Find training/fine-tuning tools."""
        query = "axolotl OR unsloth OR llama-factory stars:\u003e50"
        return self.search_repos(query, sort="stars")
    
    def get_repo_contents(self, owner: str, repo: str, 
                          path: str = "") -> List[Dict]:
        """Get contents of a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/contents/{path}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            if response.status_code == 404:
                return []
            response.raise_for_status()
            return response.json() if isinstance(response.json(), list) else [response.json()]
        except Exception as e:
            print(f"Error fetching repo contents: {e}")
            return []
    
    def check_for_modelfile(self, owner: str, repo: str) -> bool:
        """Check if repo has Ollama Modelfile."""
        contents = self.get_repo_contents(owner, repo)
        return any(file['name'].lower() == 'modelfile' for file in contents)
    
    def check_for_gguf(self, owner: str, repo: str) -> bool:
        """Check if repo contains GGUF files."""
        contents = self.get_repo_contents(owner, repo)
        
        # Check root first
        has_gguf = any(file['name'].endswith('.gguf') for file in contents)
        if has_gguf:
            return True
        
        # Check common subdirectories
        for subdir in ['models', 'quantized', 'gguf']:
            sub_contents = self.get_repo_contents(owner, repo, subdir)
            if any(file['name'].endswith('.gguf') for file in sub_contents):
                return True
        
        return False
