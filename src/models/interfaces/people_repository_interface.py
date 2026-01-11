from abc import ABC, abstractmethod
from ..sqlite.entities.people import People

class IPeopleRepository(ABC):
    @abstractmethod
    def create(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

    @abstractmethod
    def find(self, person_id: int) -> People | None:
        pass
