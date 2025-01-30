from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.utils.get_text_from_file.get_text_from_file import get_text_from_file
from src.utils.remove_linebreak_text.remove_linebreak_text import remove_linebreak_text

def send_question_to_prompt(driver, question_text):
    URL = "https://copilot.microsoft.com/chats/63RHux42QEbpix5sRYeU5"
    driver.execute_script(f"window.open('{URL}');")
    
    sleep(7)
    windows = driver.window_handles 
    driver.switch_to.window(windows[1])
    
    message_prompt = get_text_from_file('templates/prompt.txt')
    prompt_input = driver.find_element(By.XPATH, '//*[@id="userInput"]')
    message_prompt_without_line_breaks = remove_linebreak_text(message_prompt)
    prompt_input.send_keys(f'{message_prompt_without_line_breaks}. Mensagem do candidato: {question_text}')
    
    
    sleep(3)
    prompt_input.send_keys(Keys.ENTER)

    sleep(15)
