from api.core import Mixin
from ..base import db


class EnchantBase(Mixin, db.Model):
    # Determines types of enchantable items, simple subtables.
    __tablename__ = "enchantbase"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    category = db.Column(db.String)
    superCatagory = db.Column(db.String)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    abilityBonus = db.Column(db.Integer)
    price = db.Column(db.Integer)
    result = db.Column(db.String)

