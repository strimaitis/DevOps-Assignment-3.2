from flask import Flask, jsonify
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome, enter /pokedex into the base URL to see list of Pokemon")

@app.route('/pokedex')
def pokedex():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return jsonify(message="{}".format(data_json))

@app.route('/about')
def about():
    return jsonify(message="This is the about page")

@app.route('/add/<int:x>/<int:y>')
def multiply(x, y):
    result = x + y
    return jsonify(result=result)

if __name__ == '__main__':
    print("Testing for SCM polling")
    app.run(debug=True)
