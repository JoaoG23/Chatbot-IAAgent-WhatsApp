import requests
import os
import json

from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text
from src.utils.remove_emojis_text.remove_emojis_text import remove_emojis_text
from src.utils.get_text_from_file.get_text_from_file import get_text_from_file   

from src.ai.ai_connections.connections.AIConnectionInterface import AIConnectionInterface

class DeepSeekAdapter(AIConnectionInterface):
    def __init__(self):
        self.token = os.getenv('AI_TOKEN')
    
    def send_question(self, question_text):
        prompt = get_text_from_file('templates/prompt.txt')
        prompt_without_linebreak = remove_linebreak_text(prompt)

        URL = f"https://api.deepseek.com/chat/completions"  # URL corrigida
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": f"{prompt_without_linebreak}"},
                {"role": "user", "content": f"{question_text}"}
            ],
            "stream": 'false'
        }
        try:
            response = requests.post(URL, headers=headers, json=payload)
            response.raise_for_status()  
            
            if response.status_code == 200:
                response_json = response.json()
                # generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
                # text_without_linebreak = remove_linebreak_text(generated_text)
                # text_without_emojis = remove_emojis_text(text_without_linebreak)
                return 'text_without_emojis'
            return None
                
        except requests.exceptions.RequestException as e:
            raise e
        except json.JSONDecodeError as e:
            raise e
    
    def get_answer(self):
        return 'Sem implemantação para essa IA'