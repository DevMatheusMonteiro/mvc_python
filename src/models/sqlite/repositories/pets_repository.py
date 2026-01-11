from sqlalchemy.orm.exc import NoResultFound
from ..entities.pets import Pets
from ...interfaces.pet_repository_interface import IPetsRepository

class PetsRepository(IPetsRepository):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def find_all(self) -> list:
        with self.__db_connection as db:
            try:
                pets = db.session.query(Pets).all()
                return pets
            except NoResultFound:
                return []

    def delete(self, name: str) -> None:
        with self.__db_connection as db:
            try:
                db.session.query(Pets).filter(Pets.name == name).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
