from api.core import Mixin
from ..base import db


class EnchantBase(Mixin, db.Model):
    # Determines types of enchantable items, simple subtables.
    __tablename__ = "enchantbase"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    category = db.Column(db.String)
    minPercentage = db.Column(db.Integer)
    maxPercentage = db.Column(db.Integer)
    price = db.Column(db.Integer)
    result = db.Column(db.String)

