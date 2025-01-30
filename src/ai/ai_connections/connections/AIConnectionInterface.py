from abc import ABC, abstractmethod


class AIConnectionInterface(ABC):
    
    @abstractmethod
    def send_question(self):
        pass
    
    @abstractmethod
    def get_answer(self):
        pass