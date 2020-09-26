from api.core import Mixin
from .base import db


class ArmorTypeGeneration(Mixin, db.Model):
    __tablename__ = "armortypetable"
# This table determines type of armor, reference RandomArmorType (Table 3) in google sheets

    id = db.Column(db.Integer, unique=True, primary_key=True)
    minPercentage = db.Column(db.Integer)
    maxPercentage = db.Column(db.Integer)
    result = db.Column(db.String) #armorTypeName in sheets
    armorCost = db.Column(db.Integer)
    
