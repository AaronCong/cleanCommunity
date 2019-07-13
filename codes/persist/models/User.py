from codes.persist.database import db
from codes.persist.models.BaseModel import BaseModel
from flask_login import UserMixin

from codes.persist.models.Order import Order

class User(BaseModel, UserMixin):
    __tablename__='user'
    # uid = db.Column(db.Integer,primary_key=True,unique=True)
    uname = db.Column(db.String(50))
    password = db.Column(db.String(100))
    status = db.Column(db.Integer)
    phone = db.Column(db.String(50))
    apt_lat = db.Column(db.Float)
    apt_lon = db.Column(db.Float)
    cur_lat = db.Column(db.Float)
    cur_lon = db.Column(db.Float)
    oid = db.relationship('Order', backref='user')

    def __init__(self, uname, password, status, phone, apt_lat, apt_lon):
        self.uname = uname
        self.password = password
        self.apt_lat = apt_lat
        self.apt_lon = apt_lon
        self.status = status
        self.phone = phone