import requests
import os
import json

from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text
from src.utils.remove_emojis_text.remove_emojis_text import remove_emojis_text
from src.utils.get_text_from_file.get_text_from_file import get_text_from_file   


from src.ai.ai_connections.connections.AIConnectionInterface import AIConnectionInterface

class GeminiAdapter(AIConnectionInterface):
    def __init__(self):
        self.token = os.getenv('AI_TOKEN')
    
    def send_question(self, question_text):
        prompt = get_text_from_file('templates/prompt.txt')
        prompt_without_linebreak = remove_linebreak_text(prompt)

        URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.token}"  # URL corrigida
        headers = {
            "Content-Type": "application/json"
        }
        
        payload = {
            "contents": [
                {
                    "role": "assistant",
                    "parts": [
                        {
                            "text": f"{prompt_without_linebreak}"
                        }
                    ]
                },
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": f"{question_text}"
                        }
                    ]
                }
            ],
            "generation_config": {
                # "candidate_count": 1,
                "temperature": 0.7
            }
        }
        try:
            response = requests.post(URL, headers=headers, json=payload, timeout=60)
            response.raise_for_status()  # Lança exceção para status 4xx/5xx
            
            # Verifica se o conteúdo é JSON válido
            # if response.headers.get('Content-Type', 'application/json'):
            
            if response.status_code == 200:
                response_json = response.json()
                generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
                text_without_linebreak = remove_linebreak_text(generated_text)
                text_without_emojis = remove_emojis_text(text_without_linebreak)
                return text_without_emojis
            return None
                
        except requests.exceptions.RequestException as e:
            raise e
        except json.JSONDecodeError as e:
            raise e
    
    def get_answer(self):
        return 'Sem implemantação para essa IA'