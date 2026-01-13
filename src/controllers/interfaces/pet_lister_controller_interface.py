from abc import ABC, abstractmethod

class IPetListerController(ABC):
    @abstractmethod
    def list_pets(self) -> dict:
        pass
