from abc import ABC, abstractmethod

class IPetDeleterController(ABC):
    @abstractmethod
    def delete_pet(self, name: str) -> None:
        pass
