from api.core import Mixin
from ..base import db


class MagicItemTable(Mixin, db.Model):
    __tablename__ = "magicitemtable"
# For Rings, Rods, Staves, Wands
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage  = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    enchantmentPotency = db.Column(db.Integer)
    specificPiece = db.Column(db.Integer)
    meleeOrRanged = db.Column(db.Integer)
    enchantmentValue = db.Column(db.Integer)
    enchantmentCost = db.Column(db.Integer)
    result = db.Column(db.String) 
    weaponCost = db.Column(db.Integer)
