from src.utils.change_to_screen.change_to_screen import change_to_screen
from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text
from src.utils.remove_emojis_text.remove_emojis_text import remove_emojis_text

from src.ai.skip_box_do_want_signin.skip_box_do_want_signin import skip_box_do_want_signin
from src.ai.send_question_to_prompt.send_question_to_prompt import send_question_to_prompt
from src.ai.get_answer_from_prompt.get_answer_from_prompt import get_answer_from_prompt

from src.ai.ai_connections.connections.AIConnectionInterface import AIConnectionInterface

class CopilotAdapter(AIConnectionInterface):
    def __init__(self, driver):
        self.driver = driver
    
    def send_question(self, question_text):
        
        # change_to_screen(self.driver, 'ai')
            
        send_question_to_prompt(self.driver, remove_linebreak_text(question_text))
        
        skip_box_do_want_signin(self.driver)
    
    def get_answer(self):
        answer_text = get_answer_from_prompt(self.driver)
        answer_text_linebreak = remove_linebreak_text(answer_text)
        answer_text_linebreak = remove_emojis_text(answer_text_linebreak)
        return answer_text_linebreak