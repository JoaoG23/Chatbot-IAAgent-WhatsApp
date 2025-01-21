from datetime import datetime
from time import sleep
import os
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

from src.utils.logging.log_manager.log_manager import write_to_log
from src.utils.move_to_file.move_to_file import move_to_file

from src.whatsapp.do_login_whatsapp.do_login_whatsapp import do_login_whatsapp
from src.whatsapp.verify_exists_new_messages_and_return_count.verify_exists_new_messages_and_return_count import verify_exists_new_messages_and_return_count
from src.whatsapp.open_new_message_and_get_message.open_new_message_and_get_message import open_new_message_and_get_message
from src.whatsapp.send_welcome_message_in_whatsapp.send_welcome_message_in_whatsapp import send_welcome_message_in_whatsapp

options = webdriver.ChromeOptions()
user_profile = "C:\\Users\\joaog\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

options.add_argument(f"user-data-dir={user_profile}")
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

load_dotenv()

def move_contacts_to_dir_exports(source_file):
    datetime_now = datetime.now().strftime('%Y%m%d%H%M%S')
    path_file_exported = os.path.join(os.getcwd(), 'exports', datetime_now +'.xlsx')
    move_to_file(source_file, path_file_exported)




def insert_answer_to_whatsapp(driver, answer_text):
    sleep(3)
    input_message = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    input_message.send_keys(answer_text)
    sleep(2)
    input_message.send_keys(Keys.ENTER)
    sleep(14)
    

    
if __name__ == "__main__":
    try:
        do_login_whatsapp(driver)
        connect_and_create_prompt(driver)
        change_to_screen(driver, 'whatsapp')
        
        if verify_exists_new_messages_and_return_count(driver) >= 1:
            messages_found = driver.find_elements(By.CLASS_NAME, '_ahlk')
            sleep(1)
            
            for message in messages_found:
                sleep(1)
                question_text = open_new_message_and_get_message(driver, message)
                
                send_welcome_message_in_whatsapp(driver)
                
                change_to_screen(driver, 'ai')
                
                send_question_to_prompt(driver, question_text)
                
                answer_text = get_answer_from_prompt(driver)
                
                change_to_screen(driver, 'whatsapp')
                
                insert_answer_to_whatsapp(driver, answer_text)
                
                
        
            # while verify_exists_new_messages_and_return_count(driver) <= 0:
            #     sleep(3)
            #     print("Aguardando novas mensagens...")
            # sleep(2)
        # contacts_path = os.path.join(os.getcwd(), 'imports', 'contatos.xlsx')
        
        # contacts_df = get_contacts_excel(contacts_path)
        
        # clear_contacts_empty_rows_of_excel(contacts_df)
            # input_message = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]'))
    # )
    
    # sleep(10)
    # input_message.send_keys(Keys.ENTER)
        

    except WebDriverException as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    except Exception as e:
        write_to_log(traceback.format_exc(), 'error')
        print(f"Erro ao rodar automação")
    finally:
        print("Encerrando automação")
        driver.quit()   
