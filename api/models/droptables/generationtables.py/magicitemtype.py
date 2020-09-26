from api.core import Mixin
from .base import db


class MagicItemType(Mixin, db.Model):
    __tablename__ = "magicitemtype"
# This table generates the type of magic item, for reference see randommagicitem (Table 1) in google sheets 
# https://docs.google.com/spreadsheets/d/1IRZWdmj_atR4ZsiLPKaL_e5Ue78Fgb-Hfr0B1qOjd1M/edit#gid=0
    id = db.Column(db.Integer, unique=True, primary_key=True)
    encounterLevel = db.Column(db.Integer, nullable=False)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    magicQuality = db.Column(db.String, nullable=False) # Is either minor, moderate, or major
    result = db.Column(db.String, nullable=False)
    
