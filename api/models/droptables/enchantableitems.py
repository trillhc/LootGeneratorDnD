from api.core import Mixin
from ..base import db


class EnchantableItem(Mixin, db.Model):
    # This is for any table where you can get special abilities attached, weapon, armor/shield
    __tablename__ = "enchantitem"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    bonus = db.Column(db.Integer)
    price = db.Column(db.Integer)
    result = db.Column(db.String)
    category = db.Column(db.String)
