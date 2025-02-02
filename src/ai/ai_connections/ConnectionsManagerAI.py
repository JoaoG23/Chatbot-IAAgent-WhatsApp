import os
from time import sleep
from src.ai.ai_connections.connections.DeepSeekAdapter import DeepSeekAdapter
from src.ai.ai_connections.connections.GeminiAdapter import GeminiAdapter
from src.ai.ai_connections.connections.CopilotAdapter import CopilotAdapter


class ConnectionsManagerAI:
    def __init__(self, driver):
        self.ai_model = os.getenv('IA_MODEL')
        self.copilot_adapter = CopilotAdapter(driver)
        self.gemini_adapter = GeminiAdapter()
        self.deepseek_adapter = DeepSeekAdapter()
        
    def connect_ia_and_whatsapp(self, question_text):
        if self.ai_model == 'copilot':
            
            self.copilot_adapter.send_question(question_text)
            sleep(1)    
            return self.copilot_adapter.get_answer()
        
        if self.ai_model == 'gemini':
            return self.gemini_adapter.send_question(question_text)
        
        if self.ai_model == 'deepseek':
            return self.deepseek_adapter.send_question(question_text)
