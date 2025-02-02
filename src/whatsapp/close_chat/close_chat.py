from time import sleep


def close_chat(driver):
    sleep(1)
    menu_button = driver.find_element('xpath', '//*[@id="main"]/header/div[3]/div/div[2]/div/button/span')
    menu_button.click()
    sleep(0.5)
    close_button = driver.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/div/li[5]/div')
    close_button.click()
    sleep(0.5)