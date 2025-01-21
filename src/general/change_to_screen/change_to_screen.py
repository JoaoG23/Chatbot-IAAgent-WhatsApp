from time import sleep


def change_to_screen(driver, name_screen = 'whatsapp'):
    
    sleep(2)
    windows = driver.window_handles 
    if name_screen == 'ai':
        driver.switch_to.window(windows[1])
        return
    driver.switch_to.window(windows[0])
    sleep(2)