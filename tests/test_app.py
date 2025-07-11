# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app instance from the main app file
from app import app 
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome, enter /pokedex into the base URL to see list of Pokemon"}

def test_pokedex(client):
    """Test that pokedex endpoint is reached"""
    response = client.get('/pokedex')
    assert response.status_code == 200
    assert response.json ==  {"message":"{'count': 1302, 'next': 'https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20', 'previous': None, 'results': [{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'}, {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}, {'name': 'venusaur', 'url': 'https://pokeapi.co/api/v2/pokemon/3/'}, {'name': 'charmander', 'url': 'https://pokeapi.co/api/v2/pokemon/4/'}, {'name': 'charmeleon', 'url': 'https://pokeapi.co/api/v2/pokemon/5/'}, {'name': 'charizard', 'url': 'https://pokeapi.co/api/v2/pokemon/6/'}, {'name': 'squirtle', 'url': 'https://pokeapi.co/api/v2/pokemon/7/'}, {'name': 'wartortle', 'url': 'https://pokeapi.co/api/v2/pokemon/8/'}, {'name': 'blastoise', 'url': 'https://pokeapi.co/api/v2/pokemon/9/'}, {'name': 'caterpie', 'url': 'https://pokeapi.co/api/v2/pokemon/10/'}, {'name': 'metapod', 'url': 'https://pokeapi.co/api/v2/pokemon/11/'}, {'name': 'butterfree', 'url': 'https://pokeapi.co/api/v2/pokemon/12/'}, {'name': 'weedle', 'url': 'https://pokeapi.co/api/v2/pokemon/13/'}, {'name': 'kakuna', 'url': 'https://pokeapi.co/api/v2/pokemon/14/'}, {'name': 'beedrill', 'url': 'https://pokeapi.co/api/v2/pokemon/15/'}, {'name': 'pidgey', 'url': 'https://pokeapi.co/api/v2/pokemon/16/'}, {'name': 'pidgeotto', 'url': 'https://pokeapi.co/api/v2/pokemon/17/'}, {'name': 'pidgeot', 'url': 'https://pokeapi.co/api/v2/pokemon/18/'}, {'name': 'rattata', 'url': 'https://pokeapi.co/api/v2/pokemon/19/'}, {'name': 'raticate', 'url': 'https://pokeapi.co/api/v2/pokemon/20/'}]}"}

def test_about(client):
    """Test the about route."""
    response = client.get('/about')
    assert response.status_code == 200
    assert response.json == {"message": "This is the about page"}

def test_multiply(client):
    """Test the multiply route with valid input."""
    response = client.get('/add/10/4')
    assert response.status_code == 200
    assert response.json == {"result": 14}

def test_multiply_invalid_input(client):
    """Test the multiply route with invalid input."""
    response = client.get('/add/ten/four')
    assert response.status_code == 404

def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404