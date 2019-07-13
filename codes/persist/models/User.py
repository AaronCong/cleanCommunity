from codes.persist.database import db

class User(db.Model):
    __tablename__='User'
    uid = db.Column(db.Integer,primary_key=True,unique=True)
    uname = db.Column(db.String(50))
    apartment = db.Column(db.String(100))
    is_active = db.Column(db.Boolean)
    telegram = db.Column(db.String(50))

