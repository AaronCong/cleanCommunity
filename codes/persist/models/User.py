from codes.persist.database import db

class User(db.Model):
    __tablename__='User'
    uid = db.Column(db.Integer,primary_key=True,unique=True)
    uname = db.Column(db.String(50))
    is_active = db.Column(db.Boolean)
    telegram = db.Column(db.String(50))
    apt_lat = db.Column(db.Float)
    apt_lon = db.Column(db.Float)
    cur_lat = db.Column(db.Float)
    cur_lon = db.Column(db.Float)
    oid = db.relationship('Order', backref='User')