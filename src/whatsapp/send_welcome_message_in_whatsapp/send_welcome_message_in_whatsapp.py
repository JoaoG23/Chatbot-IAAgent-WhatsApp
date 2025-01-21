from time import sleep
from src.general.get_text_from_file.get_text_from_file import get_text_from_file
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_welcome_message_in_whatsapp(driver):
    welcome_text = "Olá, tudo bem? Sou Doutor Herculanos, o Cardiologista! Um momentinho, por gentileza! Já vou lhe responder.."
    # welcome_text = get_text_from_file('templates/welcome_message.txt')
    sleep(3)
    input_message = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    input_message.send_keys(welcome_text)
    sleep(2)
    input_message.send_keys(Keys.ENTER)
    sleep(3)
        