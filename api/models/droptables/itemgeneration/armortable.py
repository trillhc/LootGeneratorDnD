from api.core import Mixin
from .base import db


class ArmorGeneration(Mixin, db.Model):
    __tablename__ = "armortable"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    minPercentage = db.Column(db.Integer)
    maxPercentage = db.Column(db.Integer)
    enchantmentPotency = db.Column(db.Integer)
    specificPiece = db.Column(db.Integer)
    armorOrShield = db.Column(db.Integer)
    enchantmentValue = db.Column(db.Integer)
    enchantmentCost = db.Column(db.Integer)
    result = db.Column(db.String) 
    armorCost = db.Column(db.Integer)
    
