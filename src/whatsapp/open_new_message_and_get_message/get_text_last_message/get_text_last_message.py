from selenium.webdriver.common.by import By

def get_text_last_message(driver):
    messages_labels = driver.find_elements(By.CLASS_NAME, '_akbu')
    total_messages_labels = len(messages_labels)
    
    last_message_sended = messages_labels[total_messages_labels - 1].text
    return last_message_sended