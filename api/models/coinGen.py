from api.core import Mixin
from .base import db


class CoinGen(Mixin, db.Model):
    """Coin generation Table."""
    __tablename__ = "coingen"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    minpercentage = db.Column(db.Integer, nullable=False)
    maxpercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)


    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Person {self.name}>"