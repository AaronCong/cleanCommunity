from codes.persist.database import db

class User(db.Model):
    __tablename__='user'
    uid = db.Column(db.Integer,primary_key=True,unique=True)
    uname = db.Column(db.String(50))
    password = db.Column(db.String(100))
    is_active = db.Column(db.Boolean)
    phone = db.Column(db.String(50))
    apt_lat = db.Column(db.Float)
    apt_lon = db.Column(db.Float)
    cur_lat = db.Column(db.Float)
    cur_lon = db.Column(db.Float)
    oid = db.relationship('Order', backref='User')