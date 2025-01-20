import logging
import os
from logging.handlers import RotatingFileHandler

logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)

logger = logging.getLogger('automacao-disparo-de-mensagens-whatsapp')
logger.setLevel(logging.INFO)


log_automation_path = os.path.join(os.getcwd(), 'logs', 'logs.log')
handler = RotatingFileHandler(log_automation_path, maxBytes=5*1024*1024, backupCount=3)  # 5MB por arquivo, até 3 backups
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def write_to_log(message, type='info'):
    if type == 'error':
       return logger.error(message)
    
    return logger.info(message)

