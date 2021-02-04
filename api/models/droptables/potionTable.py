from api.core import Mixin
from ..base import db


class potionTable(Mixin, db.Model):
    __tablename__ = "potiontable"
# For Potions, Oils, Consumable Non-Spell Trigger
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage  = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    enchantmentPotency = db.Column(db.Integer)
    result = db.Column(db.String)
    itemCost = db.Column(db.Integer)