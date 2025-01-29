from datetime import datetime
import os
from time import sleep
import traceback
from dotenv import load_dotenv

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from src.ai.get_answer_from_prompt.get_answer_from_prompt import get_answer_from_prompt
from src.ai.send_question_to_prompt.send_question_to_prompt import send_question_to_prompt
from src.ai.connect_and_create_prompt.connect_and_create_prompt import connect_and_create_prompt
from src.ai.skip_box_do_want_signin.skip_box_do_want_signin import skip_box_do_want_signin

from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text
from src.utils.remove_emojis_text.remove_emojis_text import remove_emojis_text
from src.utils.change_to_screen.change_to_screen import change_to_screen
from src.utils.logging.log_manager.log_manager import write_to_log

from src.whatsapp.do_login_whatsapp.do_login_whatsapp import do_login_whatsapp
from src.whatsapp.verify_exists_new_messages_and_return_count.verify_exists_new_messages_and_return_count import verify_exists_new_messages_and_return_count
from src.whatsapp.open_new_message_and_get_message.open_new_message_and_get_message import open_new_message_and_get_message
from src.whatsapp.send_loading_message_in_whatsapp.send_loading_message_in_whatsapp import send_loading_message_in_whatsapp
from src.whatsapp.insert_answer_to_whatsapp.insert_answer_to_whatsapp import insert_answer_to_whatsapp
from src.whatsapp.close_chat.close_chat import close_chat
# from src.whatsapp.send_message_to_whatsapp.send_message_to_whatsapp import send_message_to_whatsapp

load_dotenv()

user_profile = os.getenv('PATH_USER_PROFILE_CHROME')

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_profile}")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def exchange_messages_between_whatsapp_and_ai(driver):
    if verify_exists_new_messages_and_return_count(driver) >= 1:
        messages_found = driver.find_elements(By.CLASS_NAME, '_ahlk')
        sleep(1)
        messages_found.reverse()
            
        for message in messages_found:
            sleep(1)
            question_text = open_new_message_and_get_message(driver, message)
            
            send_loading_message_in_whatsapp(driver)
            
            change_to_screen(driver, 'ai')
            
            send_question_to_prompt(driver, remove_linebreak_text(question_text))
            
            skip_box_do_want_signin(driver)

            answer_text = get_answer_from_prompt(driver)
            answer_text_linebreak = remove_linebreak_text(answer_text)
            answer_text_linebreak = remove_emojis_text(answer_text_linebreak)
            
            change_to_screen(driver, 'whatsapp')
            
            insert_answer_to_whatsapp(driver, answer_text_linebreak)
            
            close_chat(driver)
            
if __name__ == "__main__":
    try:
        connect_and_create_prompt(driver)
        
        change_to_screen(driver, 'whatsapp')
        
        do_login_whatsapp(driver)
        
        while True:
            exchange_messages_between_whatsapp_and_ai(driver)
            sleep(2)

    except WebDriverException as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    except Exception as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    finally:
        print("Encerrando automação")
        driver.quit()   
