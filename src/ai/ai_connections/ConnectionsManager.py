from src.ai.ai_connections.connections.AIConnectionInterface import AIConnectionInterface
from src.ai.ai_connections.connections.CopilotAdapter import CopilotAdapter


class ConnectionsManager:
    def __init__(self, driver):
        self.ai_model = 'copilot'
        self.copilotAdapter = CopilotAdapter(driver)
    
    def select_ai_send_question(self, question_text):
        if self.ai_model == 'copilot':
            self.copilotAdapter.send_question(question_text)
            
    def select_ai_get_answer(self):
        if self.ai_model == 'copilot':
            return self.copilotAdapter.get_answer()
