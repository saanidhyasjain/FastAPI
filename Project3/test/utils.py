
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, Users
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
    )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'saanidhya09', 'id' : 1, 'user_role' : 'admin'}


# Changing the dependency on test and wrapping it within test client so app knows its test
client = TestClient(app)


@pytest.fixture
def test_todo():
    todo = Todos(
        title='learn fastapi',
        description='evryday',
        priority=5,
        complete=False,
        owner_id=1
    )

    db = TestingSessionLocal()  # always make sure to add testing db connection, if production db given the all the tables from main db will be deleted
    db.add(todo)
    db.commit()

    yield todo # will run untill end of the function

    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    user =  Users(
                email = 'saanidhya.s@mail.com',
                username =  'saanidhya',
                first_name =  'saanidhya',
                last_name =  's',
                hashed_password =  bcrypt_context.hash('test1234'),
                is_active = True,
                role =  'admin',
                phone_number =  '9353617550',
                address =  'mangalore'
                )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()

    yield user

    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()

