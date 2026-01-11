from sqlalchemy.orm.exc import NoResultFound
from ..entities.people import People
from ..entities.pets import Pets

class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create(self,first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_connection as db:
            try:
                data = People(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_id=pet_id
                )
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def get_by_id(self, person_id: int) -> People | None:
        with self.__db_connection as db:
            try:
                person = (
                    db.session
                        .query(People)
                        .outerjoin(Pets, Pets.id == People.pet_id)
                        .filter(People.id == person_id)
                        .with_entities(
                            People.first_name,
                            People.last_name,
                            Pets.name.label("pet_name"),
                            Pets.type.label("pet_type")
                        ).one()
                )
                return person
            except NoResultFound:
                return None
