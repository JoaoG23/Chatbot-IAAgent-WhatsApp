from selenium.webdriver.common.by import By

def verify_exists_new_messages_and_return_count(driver):
    messages_found = driver.find_elements(By.CLASS_NAME, '_ahlk')
    return len(messages_found)