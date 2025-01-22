from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_question_to_prompt(driver, question_text):
    sleep(2)
    prompt_input = driver.find_element(By.XPATH, '//*[@id="userInput"]')
    prompt_input.send_keys(question_text)
    
    sleep(3)
    prompt_input.send_keys(Keys.ENTER)

    sleep(15)
