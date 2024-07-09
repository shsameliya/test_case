import pytest
from app import db 
from app.models import User

# def test_create_user(client):
#     # Test creating a new user
#     response = client.post('/user', data={'username': 'user1@gmail.com', 'password': 'user1@123'})
#     assert response.status_code == 201
#     assert b'user created' in response.data


#user is function name of conftets.py file
def test_model_fixture(user):
    assert user.username == "Charles Dickens"
    assert user.password == "user@gmail.com"


def test_post_new_user(client):
    data = {  'password': 'password' }
    response = client.post('/user', data=data)
    assert response.status_code == 400
    assert 'username required' in response.json['message']

    data = { 'username': 'username'}
    response = client.post('/user', data=data)
    print('response .. ',response)
    assert response.status_code == 400
    assert 'username required' in response.json['message']

    data = { 'username': 'user@gmail.com', 'password': 'password' }
    response = client.post('/user', data=data)
    assert response.status_code == 201
    assert 'user created' in response.json['message']

    data = { 'username': 'user@gmail.com', 'password': 'password' }
    response = client.post('/user', data=data)
    assert response.status_code == 500
    assert 'error creating user' in response.json['message']


def test_login(client):
    response = client.post('/login', data={'username': 'user@gmail.com', 'password': 'password'})
    assert response.status_code == 200
    assert b'Login successful' in response.data

    response = client.post('/login', data={'password': 'user@123'})
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data

    response = client.post('/login', data={'username': 'user@gmail.com'})
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data

    response = client.post('/login', data={'username': 'user@gmail.com', 'password': 'wrong_password'})
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data



def test_logout(client):
    response = client.post('/logout')
    assert response.status_code == 200
    assert b'Logout successful' in response.data


def test_delet_user(client):
    data = { 'username': 'user@gmail.com', 'password': 'password' }
    response = client.delete('/user', data=data)
    assert response.status_code == 200
    assert 'user deleted' in response.json['message']



# import factory
# from pytest_factoryboy import register

# @register
# class AuthorFactory(factory.Factory):
#     class Meta:
#         model = User

#     username = "Charles Dickens",
#     email = "user@gmail.com"



@pytest.mark.parametrize("test_input,expected", [("3+8", 11), ('8+2',10), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# @pytest.mark.parametrize("user__username", ["Bill Gates"])
# def test_model_fixture(user):
#     assert user.username == "Bill Gates"


# @pytest.mark.parametrize("user__username", ["Bill Gates"])
# # @pytest.mark.parametrize("user", [{"username": "Bill Gates"}])
# def test_model_fixture(user):
#     assert user.username == "Bill Gates"

