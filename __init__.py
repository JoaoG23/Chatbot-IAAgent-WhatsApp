from datetime import datetime
from time import sleep
import traceback
from dotenv import load_dotenv

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.general.change_to_screen.change_to_screen import change_to_screen

from src.ai.get_answer_from_prompt.get_answer_from_prompt import get_answer_from_prompt
from src.ai.send_question_to_prompt.send_question_to_prompt import send_question_to_prompt
from src.ai.connect_and_create_prompt.connect_and_create_prompt import connect_and_create_prompt
from src.ai.skip_box_do_want_signin.skip_box_do_want_signin import skip_box_do_want_signin

from src.utils.logging.log_manager.log_manager import write_to_log

from src.whatsapp.do_login_whatsapp.do_login_whatsapp import do_login_whatsapp
from src.whatsapp.verify_exists_new_messages_and_return_count.verify_exists_new_messages_and_return_count import verify_exists_new_messages_and_return_count
from src.whatsapp.open_new_message_and_get_message.open_new_message_and_get_message import open_new_message_and_get_message
from src.whatsapp.send_loading_message_in_whatsapp.send_loading_message_in_whatsapp import send_loading_message_in_whatsapp
from src.whatsapp.insert_answer_to_whatsapp.insert_answer_to_whatsapp import insert_answer_to_whatsapp

options = webdriver.ChromeOptions()
user_profile = "C:\\Users\\joaog\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

options.add_argument(f"user-data-dir={user_profile}")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

load_dotenv()


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
            
            send_question_to_prompt(driver, question_text)
            
            skip_box_do_want_signin(driver)

            answer_text = get_answer_from_prompt(driver)
            answer_text_linebreak = answer_text.replace("\n", " ")
            
            change_to_screen(driver, 'whatsapp')
            
            insert_answer_to_whatsapp(driver, answer_text_linebreak)
            
            write_to_log(f'Question: {question_text} to Response: {answer_text}')


if __name__ == "__main__":
    try:
        do_login_whatsapp(driver)
        connect_and_create_prompt(driver)
        change_to_screen(driver, 'whatsapp')
        
        exists_messages_in_whatsapp = 0
        while exists_messages_in_whatsapp < 1:
            sleep(5)
            print('Waiting for new messages...')
            exists_messages_in_whatsapp = verify_exists_new_messages_and_return_count(driver)
        sleep(2)
        exchange_messages_between_whatsapp_and_ai(driver)
             
        # if verify_exists_new_messages_and_return_count(driver) >= 1:
        #     messages_found = driver.find_elements(By.CLASS_NAME, '_ahlk')
        #     sleep(1)
        #     messages_found.reverse()
            
        #     for message in messages_found:
        #         sleep(1)
        #         question_text = open_new_message_and_get_message(driver, message)
                
        #         send_loading_message_in_whatsapp(driver)
                
        #         change_to_screen(driver, 'ai')
                
        #         send_question_to_prompt(driver, question_text)
                
        #         skip_box_do_want_signin(driver)
                
        #         answer_text = get_answer_from_prompt(driver)
        #         answer_text_linebreak = answer_text.replace("\n", " ")
                
        #         change_to_screen(driver, 'whatsapp')
                
        #         insert_answer_to_whatsapp(driver, answer_text_linebreak)
                
        #         write_to_log(f'Question: {question_text} to Response: {answer_text}')
        
# box # //*[@id="app"]/main/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div
# button //*[@id="app"]/main/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/button[2]
# title="Talvez mais tarde"
    except WebDriverException as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    except Exception as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    finally:
        print("Encerrando automação")
        driver.quit()   
