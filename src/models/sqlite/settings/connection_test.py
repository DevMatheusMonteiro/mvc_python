import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

@pytest.mark.skip(reason="Skipping DB connection test for now")
def test_connect_to_db():
    assert db_connection_handler.engine is None
    db_connection_handler.connect()
    db_engine = db_connection_handler.engine
    assert db_engine is not None
    assert isinstance(db_engine, Engine)
