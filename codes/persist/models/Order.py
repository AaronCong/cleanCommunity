from codes.persist.database import db

class Order(db.Model):
    __tablename__='order'
    oid = db.Column(db.Integer,primary_key=True,unique=True)
    uid1 = db.Column(db.Integer, db.ForeignKey('user.uid'))
    uid2 = db.Column(db.Integer, db.ForeignKey('user.uid'))
