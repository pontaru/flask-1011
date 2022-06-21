# wsgi.py

from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Billy'},
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def return_products():
    return jsonify(PRODUCTS)