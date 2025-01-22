from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def insert_answer_to_whatsapp(driver, answer_text):
    sleep(3)
    input_message = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    input_message.send_keys(answer_text)
    sleep(2)
    input_message.send_keys(Keys.ENTER)
    sleep(19)
    
