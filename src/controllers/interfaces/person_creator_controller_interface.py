from abc import ABC, abstractmethod

class IPersonCreatorController(ABC):

    @abstractmethod
    def create(self, data: dict) -> dict:
        pass
