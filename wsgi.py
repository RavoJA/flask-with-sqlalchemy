#import os
#import logging
#logging.warn(os.environ["DUMMY"])

# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from models import Product

from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200