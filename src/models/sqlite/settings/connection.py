from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None

    @property
    def engine(self):
        return self.__engine

    def connect(self):
        if self.__engine is None:
            self.__engine = create_engine(self.__connection_string)
        return self.__engine

db_connection_handler = DBConnectionHandler()
