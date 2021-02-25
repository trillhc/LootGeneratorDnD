from api.core import Mixin
from ..base import db


class ItemMagicChance(Mixin, db.Model):
    __tablename__ = "itemmagicchance"
    # For determining how many mundane, minor, medium or major magical items you get

    id = db.Column(db.Integer, unique=True, primary_key=True)
    encounterLevel = db.Column(db.Integer, nullable=True)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)
    magicalness = db.Column(db.String, nullable=False)
