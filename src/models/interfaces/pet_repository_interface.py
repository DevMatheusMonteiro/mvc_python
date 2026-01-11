from abc import ABC, abstractmethod
from ..sqlite.entities.pets import Pets

class IPetsRepository(ABC):
    @abstractmethod
    def list(self) -> list[Pets]:
        pass
    @abstractmethod
    def delete(self, name: str) -> None:
        pass
