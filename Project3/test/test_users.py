from .utils import *
from ..routers.users import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['email'] == 'saanidhya.s@mail.com'
    assert response.json()['username'] == 'saanidhya'
    assert response.json()['first_name'] ==  'saanidhya'
    assert response.json()['last_name'] == 's'
    assert response.json()['is_active'] == True
    assert response.json()['role'] ==  'admin'
    assert response.json()['phone_number'] =='9353617550'
    assert response.json()['address'] == 'mangalore'



def test_change_password_success(test_user):
    response = client.put('users/password', json={'password':'test1234', 'new_password':'newpassword'})
    assert response.status_code == 204

def test_invalid_current_password_while_change(test_user):
    response = client.put('users/password', json={'password':'test12h34', 'new_password':'newpassword'})
    assert response.status_code == 401
    assert response.json() == {'detail':'error on password change'}

def test_change_phone_number(test_user):
    response = client.put("users/phone_number/9353617550")
    assert response.status_code == 204
