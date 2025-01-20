from time import sleep
from selenium.webdriver.common.by import By


def do_login_whatsapp(driver):
    driver.get("https://web.whatsapp.com")
    while len(driver.find_elements(By.ID, 'side')) < 1:
        sleep(1)
        print('Abra o celular e escaneie o QR Code na tela por favor!..')
        print("WhatsApp carregado com sucesso.")
    sleep(2)