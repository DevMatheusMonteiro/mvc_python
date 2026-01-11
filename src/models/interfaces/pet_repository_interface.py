from abc import ABC, abstractmethod
from ..sqlite.entities.pets import Pets

class IPetsRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Pets]:
        pass
    @abstractmethod
    def delete(self, name: str) -> None:
        pass
