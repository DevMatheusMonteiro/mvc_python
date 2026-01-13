from abc import ABC, abstractmethod

class IPersonFinderController(ABC):
    @abstractmethod
    def find(self, person_id: int) -> dict:
        pass
