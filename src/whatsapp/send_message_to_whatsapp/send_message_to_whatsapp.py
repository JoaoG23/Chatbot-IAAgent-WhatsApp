from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.utils.get_text_from_file.get_text_from_file import get_text_from_file

def send_message_to_whatsapp(driver):
    sleep(1)
    message_text = get_text_from_file('templates/message.txt')

    input_message = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    input_message.send_keys(message_text)
    sleep(1)
    input_message.send_keys(Keys.ENTER)
    sleep(3)
    
