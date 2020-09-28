from api.core import Mixin
from .base import db


class MundaneItem(Mixin, db.Model):
    __tablename__ = "mundaneitem"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    itemName = db.Column(db.String, nullable=False)
    itemType = db.Column(db.String, nullable=False)
    itemCost = db.Column(db.Integer, nullable=False)
    itemCostToCreate = db.Column(db.Integer, nullable=False)
    itemCasterLevel = db.Column(db.Integer, nullable=False)
    itemFeatNeeded = db.Column(db.String, nullable=False)
    itemSpellsNeeded = db.Column(db.String, nullable=False)
    itemLevelRecommended = db.Column(db.Integer, nullable=False)
    itemDescription = db.Column(db.String, nullable=False)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)


    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return f"<id {self.id}>"
