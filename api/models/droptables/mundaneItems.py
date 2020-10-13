from api.core import Mixin
from ..base import db


class MundaneItem(Mixin, db.Model):
    __tablename__ = "mundaneitem"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    itemName = db.Column(db.String, nullable=False)
    #itemClass is "init" for initial roll then "armor" or "tools" ect.
    itemClass = db.Column(db.String)
    itemCost = db.Column(db.Integer)
    itemCostToCreate = db.Column(db.Integer)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)


    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return f"<id {self.id}>"
