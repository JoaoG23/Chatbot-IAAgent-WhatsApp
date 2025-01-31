from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.utils.get_text_from_file.get_text_from_file import get_text_from_file
from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text
from src.utils.wait_for_element_load.wait_for_element_load import wait_for_element_load

def send_question_to_prompt(driver, question_text):
    
    windows = driver.window_handles 
    if len(windows) < 2:
        URL = "https://copilot.microsoft.com/chats/"
        driver.execute_script(f"window.open('{URL}');")
    sleep(10)
    
    windows = driver.window_handles 
    driver.switch_to.window(windows[1])
    wait_for_element_load(driver.find_elements(By.XPATH, '//*[@id="userInput"]'), 'Input Prompt')
    
    message_prompt = get_text_from_file('templates/prompt.txt')
    prompt_input = driver.find_element(By.XPATH, '//*[@id="userInput"]')
    message_prompt_without_line_breaks = remove_linebreak_text(message_prompt)
    prompt_input.send_keys(f'{message_prompt_without_line_breaks}. Dúvida: {question_text}')
    
    sleep(2)
    prompt_input.send_keys(Keys.ENTER)

    sleep(8)
