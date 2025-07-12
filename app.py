'''
  App.py: Application that displays home web page, accesses pokemon data from API endpoints 
  and adds numbers
'''

from urllib.request import urlopen
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    Displays instructions on how to access /pokedex
    Args: N/A
    """
    return jsonify(message="Welcome, enter /pokedex into the base URL to see list of Pokemon")

@app.route('/pokedex')
def pokedex():
    """
    Displays pokemon from endpoint
    Args: N/A
    """
    url = "https://pokeapi.co/api/v2/pokemon/"
    with urlopen(url) as response:
        read_response = response.read()
        data_json = json.loads(read_response)
        return jsonify(message=f"{data_json}")

@app.route('/about')
def about():
    """
    Displays static json
    Args: N/A
    """
    return jsonify(message="This is the about page")

@app.route('/add/<int:x>/<int:y>')
def multiply(x, y):
    """
    Returns the sum of two integers
    Args:
    x: Integer
    y: Integer
    """
    result = x + y
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
