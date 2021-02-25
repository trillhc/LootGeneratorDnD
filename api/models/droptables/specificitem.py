from api.core import Mixin
from ..base import db


class SpecificItem(Mixin, db.Model):
    # Specific weapons, armor, sheilds and wonderouse items
    __tablename__ = "specificitem"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    bonus = db.Column(db.Integer)
    price = db.Column(db.Integer)
    name = db.Column(db.String)
    magicalness = db.Column(db.String)
    #weapon, armor, sheild or wonderous
    category = db.Column(db.String)
