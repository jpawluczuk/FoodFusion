import pytest
from app import create_app, db

@pytest.fixture()
def app():
    app = create_app("mysql://")
    with app.app_context():
        db.create_all()
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
