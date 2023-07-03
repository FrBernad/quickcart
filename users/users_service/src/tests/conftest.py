import pytest
from src.api.persistence.db import db
from src import create_app
from unittest.mock import Mock
from src.api.persistence.user_dao_impl import UserDaoImpl
from flask_sqlalchemy import SQLAlchemy
from unittest.mock import MagicMock

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        yield app.test_client()


@pytest.fixture(scope="test")
def test_user_dao():
    from src.api.persistence.user_dao_impl import UserDaoImpl

    db_mock = Mock()
    db_session = Mock()
    db_commit = Mock()
    db_add = Mock()
    db_session.commit = db_commit
    db_session.add = db_add
    db_mock.session = db_session
    dao = UserDaoImpl(db_mock)
    yield dao, db_mock


@pytest.fixture(scope="module")
def test_user_service():
    from src.api.services.user_service_impl import UserServiceImpl

    user_dao_mock = Mock(spec=UserDaoImpl)
    service = UserServiceImpl(user_dao_mock)
    yield service, user_dao_mock


@pytest.fixture(scope="function")
def test_database():
    from src.api.models.users import User

    db.drop_all()
    db.create_all()
    yield db 
    db.session.remove()
    db.drop_all()
