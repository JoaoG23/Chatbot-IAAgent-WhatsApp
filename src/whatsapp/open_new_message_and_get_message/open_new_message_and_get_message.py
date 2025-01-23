from time import sleep

from selenium.webdriver.common.by import By

from src.whatsapp.open_new_message_and_get_message.get_text_last_message.get_text_last_message import get_text_last_message

def open_new_message_and_get_message(driver, message):

    sleep(1)
    message.click()
    sleep(2)
    
    message_labels = driver.find_elements(By.CLASS_NAME, '_akbu')
    
    if len(message_labels) > 0:
        sleep(5)
        message_text = get_text_last_message(driver)
        sleep(1)
        return message_text