from codes.persist.database import db
from codes.persist.models.BaseModel import BaseModel

class Order(BaseModel):
    __tablename__='order'
    # oid = db.Column(db.Integer,primary_key=True,unique=True)
    uid1 = db.Column(db.Integer, db.ForeignKey('user.id'))
    uid2 = db.Column(db.Integer)
