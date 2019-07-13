from codes.persist.database import db

class Dialog(db.Model):
    __tablename__='dialog'
    did = db.Column(db.Integer,primary_key=True,unique=True)
    uid1 = db.ForeignKey(db.Integer, db.ForeignKey('user.uid'))
    uid2 = db.ForeignKey(db.Integer, db.ForeignKey('user.uid'))
    utterance = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default = db.func.now())
    oid = db.ForeignKey(db.Integer, db.ForeignKey('order.oid'))

