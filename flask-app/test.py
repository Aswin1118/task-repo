from list import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Apples' in response.data
    assert b'Bananas' in response.data
    assert b'Oranges' in response.data

def test_index_post_add(client):
    response = client.post('/', data={'new_item': 'Pears'})
    assert response.status_code == 200
    assert b'Pears' in response.data

def test_index_post_remove(client):
    response = client.post('/', data={'remove_item': 'Apples'})
    assert response.status_code == 200
    assert b'Apples' not in response.data
    assert b'Bananas' in response.data
    assert b'Oranges' in response.data
