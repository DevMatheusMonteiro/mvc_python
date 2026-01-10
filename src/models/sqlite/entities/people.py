from sqlalchemy import Column, BIGINT, String, ForeignKey
from ..settings.base import Base

class People(Base):
    __tablename__ = "people"

    id: Column = Column(BIGINT, primary_key=True, autoincrement=True)
    first_name: Column = Column(String, nullable=False)
    last_name: Column = Column(String, nullable=False)
    age: Column = Column(BIGINT, nullable=False)
    pet_id: Column = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self) -> str:
        return f"""People(id={self.id},
        first_name='{self.first_name}',
        last_name='{self.last_name}',
        age={self.age}, pet_id={self.pet_id})"""
