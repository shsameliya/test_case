import pytest
from app import app, db  # Adjust the import path based on your project structure
from app.models import User


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
