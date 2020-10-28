from api.core import Mixin
from ..base import db


class ItemMagicGod(Mixin, db.Model):
    # This table is the god table, used to generate type of magical items
    __tablename__ = "magicgod"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    result = db.Column(db.String)
    
