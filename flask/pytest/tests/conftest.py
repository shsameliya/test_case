import pytest, factory
from pytest_factoryboy import register
from app.models import User 
from app import app,db


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# from faker import Faker

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()
#             yield client
#         with app.app_context():
#             db.session.remove()
#             db.drop_all()





@register
class AuthorFactory(factory.Factory):
    class Meta:
        model = User

    username = "Charles Dickens"
    password = "user@gmail.com"

# @pytest.fixture
# def user(author_factory):
#     return author_factory()

@pytest.fixture
def user():
    return AuthorFactory()