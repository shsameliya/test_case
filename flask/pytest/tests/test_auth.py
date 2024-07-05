import pytest
# from app import app, db
from app import db 
from app.models import User


def test_login(client):

    response = client.post('/login', data={'username': 'user@gmail.com', 'password': 'user@123'})
    print('check...',response)
    assert response.status_code == 200
    assert b'Login successful' in response.data

def test_logout(client):
    response = client.post('/logout')
    assert response.status_code == 200
    assert b'Logout successful' in response.data

