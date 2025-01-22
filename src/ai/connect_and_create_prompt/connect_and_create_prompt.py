from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.general.get_text_from_file.get_text_from_file import get_text_from_file


def connect_and_create_prompt(driver):
    URL = "https://copilot.microsoft.com/chats/63RHux42QEbpix5sRYeU5"
    driver.execute_script(f"window.open('{URL}');")
    
    sleep(1)
    windows = driver.window_handles 
    driver.switch_to.window(windows[1])
    sleep(14)
    # message_prompt = """Quero que atue como um Doutor chamado Carlos Xipoca, Cardiologista, quero que ajude a sanar as duvidas dos pacientes, com base nas mensagens que irei lhe enviar. Observação: Seja simples, objetivo, respostas curtas, no maximo 4 linhas"""
    message_prompt = get_text_from_file('templates/prompt.txt')
    prompt_input = driver.find_element(By.XPATH, '//*[@id="userInput"]')
    prompt_input.send_keys(message_prompt)
    
    sleep(2)
    prompt_input.send_keys(Keys.ENTER)
    sleep(7)
    