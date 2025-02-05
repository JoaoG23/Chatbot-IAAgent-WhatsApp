import os
from time import sleep
import traceback
from dotenv import load_dotenv

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from src.ai.ai_connections.ConnectionsManagerAI import ConnectionsManagerAI

from src.utils.change_to_screen.change_to_screen import change_to_screen
from src.utils.logging.log_manager.log_manager import write_to_log

from src.whatsapp.do_login_whatsapp.do_login_whatsapp import do_login_whatsapp
from src.whatsapp.verify_exists_new_messages_and_return_count.verify_exists_new_messages_and_return_count import verify_exists_new_messages_and_return_count
from src.whatsapp.open_new_message_and_get_message.open_new_message_and_get_message import open_new_message_and_get_message
from src.whatsapp.send_loading_message_in_whatsapp.send_loading_message_in_whatsapp import send_loading_message_in_whatsapp
from src.whatsapp.insert_answer_to_whatsapp.insert_answer_to_whatsapp import insert_answer_to_whatsapp
from src.whatsapp.close_chat.close_chat import close_chat

load_dotenv()

user_profile = os.getenv('PATH_USER_PROFILE_CHROME')

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_profile}")
options.add_argument("--headless==new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

class ChatbotIAAgentWhatsApp:
    def __init__(self):
        self.driver = driver
        
    def exchange_messages_between_whatsapp_and_ai(self):
        
        ai = ConnectionsManagerAI(self.driver)
        if verify_exists_new_messages_and_return_count(self.driver) >= 1:
            messages_found = self.driver.find_elements(By.CLASS_NAME, '_ahlk')
            sleep(1)
            messages_found.reverse()
                
            for message in messages_found:
                sleep(1)
                # WHATSAPP
                question_text = open_new_message_and_get_message(self.driver, message)
                sleep(8)
                send_loading_message_in_whatsapp(self.driver)
                
                # IA
                answer_text = ai.connect_ia_and_whatsapp(question_text)
                
                change_to_screen(self.driver, 'whatsapp')
                # WHATSAPP
                insert_answer_to_whatsapp(self.driver, answer_text)
                
                close_chat(self.driver)
    
    def run_automation(self):
        # connect_and_create_prompt(self.driver)
        
        change_to_screen(self.driver, 'whatsapp')
        
        do_login_whatsapp(self.driver)
        
        while True:
            self.exchange_messages_between_whatsapp_and_ai()
            sleep(6)
            
if __name__ == "__main__":
    try:
        ChatbotIAAgentWhatsApp().run_automation()

    except WebDriverException as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    except Exception as e:
        write_to_log(traceback.format_exc(), 'error')
        # print(f"Erro ao rodar automação")
        print(e)
    finally:
        print("Encerrando automação")
        driver.quit()   
