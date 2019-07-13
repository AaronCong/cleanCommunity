from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from codes.persist.database import db
from codes.persist.models import *
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI

if __name__ == '__main__':
    db.app = app
    db.init_app(app)
    db.create_all()