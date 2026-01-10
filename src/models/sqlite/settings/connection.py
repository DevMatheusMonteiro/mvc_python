from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    @property
    def engine(self):
        return self.__engine

    def connect(self):
        if self.__engine is None:
            self.__engine = create_engine(self.__connection_string)
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.connect())
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.session:
            self.session.close()

db_connection_handler = DBConnectionHandler()
