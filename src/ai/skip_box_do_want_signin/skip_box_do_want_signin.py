from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def skip_box_do_want_signin(driver):
    sleep(2) 
    button_open_exists = len(driver.find_elements(By.XPATH, '//*[@id="app"]/main/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/button[2]')) > 0
    if button_open_exists:
        sleep(2)
        button_try_later = driver.find_element(By.XPATH, "//button[@title='Talvez mais tarde']")
        button_try_later.click()