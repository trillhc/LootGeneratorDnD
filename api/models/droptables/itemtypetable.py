from api.core import Mixin
from .base import db


class ItemTypeTable(Mixin, db.Model):
    # This table is used to determine types (armor/shield and melee/ranged)
    __tablename__ = "itemtype"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    typeArmor = db.Column(db.Integer)
    typeShield = db.Column(db.Integer)
    typeMeleeWeapon = db.Column(db.Integer)
    typeRangeWeapon = db.Column(db.Integer)
    minPercentage = db.Column(db.Integer)
    maxPercentage = db.Column(db.Integer)
    result = db.Column(db.String)
    
