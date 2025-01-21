
from time import sleep
from selenium.webdriver.common.by import By

def get_answer_from_prompt(driver):

    sleep(1)
    
    box_messages = driver.find_elements(By.CLASS_NAME, 'space-y-3')
    
    answer = ''
    verify_exists_messages = len(box_messages) > 0
    if verify_exists_messages:
        sleep(2)
        last_message = box_messages[len(box_messages) - 1]
        
        answer = last_message.text
        sleep(2)
        
    return answer

        