from api.core import Mixin
from ..base import db


class ItemTypeTable(Mixin, db.Model):
    # This table is the god table, used to generate type of magical items
    __tablename__ = "itemtype"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    supercatagory = db.Column(db.Boolean)
    itemName = db.Column(db.String) 
    itemMagicalness = db.Column(db.String)   # minor, medium, or major
    itemEnchantType = db.Column(db.String)   # does the enchant belong on weapon, armor, shield, etc?
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercebtage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    itemCost = db.Column(db.Integer)     
    costCreate = db.Column(db.Integer)   # the cost to create is half of the cost.

    result = db.Column(db.String)
    