from sqlalchemy import Column, BIGINT, String
from ..settings.base import Base

class Pets(Base):
    __tablename__ = "pets"

    id: Column = Column(BIGINT, primary_key=True, autoincrement=True)
    name: Column = Column(String, nullable=False)
    type: Column = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Pet(id={self.id}, name='{self.name}', type='{self.type}')"
