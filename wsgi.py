# wsgi.py

from flask import Flask, jsonify, abort, request
import itertools

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Billy'},
}

START_INDEX = len(PRODUCTS) + 1
IDENTIFIER_GENERATOR = itertools.count(START_INDEX)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def return_products():
    return jsonify(PRODUCTS), 200

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def return_one_product(id):
    product = PRODUCTS.get(id)
    
    if product is None:
        abort(404)
    return jsonify(product), 200

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def remove_product(id):
    product = PRODUCTS.pop(id, None)
    if product is None:
        abort(404)        
    return '', 204

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    if data is None: 
        abort(404)
        
    name = data.get('name')
    
    if  name is None:
        abort(400)
    
    if name == '' or not instance(name, str):
        abort(422)
    
    next_id = next(IDENTIFIER_GENERATOR)
    
    PRODUCTS[next_id] = {'id': next_id, 'name':name}
    
    return jsonify(PRODUCTS[next_id]), 201

@app.route('/api/v1/products/<int:id>', methods=['PATCH'])
def update_one_product(product_id):
    
    data = request.get_json()
    
    if data is None:
        abort(400)

    name = data.get('name')

    if name is None:
        abort(400)

    if name == '' or not isinstance(name, str):
        abort(422)

    product = PRODUCTS.get(product_id)

    if product is None:
        abort(404)

    PRODUCTS[product_id]['name'] = name

    return '', 204
