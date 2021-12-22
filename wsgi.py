#import os
#import logging
#logging.warn(os.environ["DUMMY"])

# wsgi.py
# pylint: disable=missing-docstring
BASE_URL = '/api/v1'

from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  # NEW LINE (L'ordre est important ici !)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import many_product_schema, one_product_schema

from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products/<id>', methods=['GET'])
def get_one_product(id):
    product = db.session.query(Product).get(id)   
    return one_product_schema.jsonify(product), 200

@app.route(f'{BASE_URL}/products/delete/<id>', methods=['DELETE'])
def delete_one_product(id):
    product = db.session.query(Product).get(id)
    db.session.query(Product).delete(product)
    return "Product removed", 200

@app.route(f'{BASE_URL}/products/add', methods=['POST'])
def add_one_product(id):
    product = Product(10, 'ORANGE')
    db.session.add(product)
    db.session.commit()
    return "Product added", 200

@app.route(f'{BASE_URL}/products/update', methods=['PUT'])
def update_one_product(id):
    return "Product Updated", 200