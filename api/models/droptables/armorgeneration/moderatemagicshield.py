from api.core import Mixin
from .base import db


class ModerateMagicShield(Mixin, db.Model):
    __tablename__ = "moderatemagicshield"


    id = db.Column(db.Integer, unique=True, primary_key=True)
    encounterLevel = db.Column(db.Integer, nullable=False)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)
    
