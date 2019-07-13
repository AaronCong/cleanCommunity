from codes.persist.database import db
from codes.persist.models.BaseModel import BaseModel

class Dialog(BaseModel):
    __tablename__='dialog'
    # did = db.Column(db.Integer,primary_key=True,unique=True)
    uid1 = db.Column(db.Integer, db.ForeignKey('user.id'))
    uid2 = db.Column(db.Integer)
    utterance = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default = db.func.now())
    oid = db.Column(db.Integer, db.ForeignKey('order.id'))

