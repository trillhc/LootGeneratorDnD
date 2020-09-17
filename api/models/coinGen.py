from api.core import Mixin
from .base import db


class CoinGen(Mixin, db.Model):
    __tablename__ = "coingen"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    minpercentage = db.Column(db.Integer, nullable=False)
    maxpercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)


    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return f"<id {self.id}>"