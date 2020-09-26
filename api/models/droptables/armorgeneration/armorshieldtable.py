from api.core import Mixin
from .base import db


class ArmorShieldTable(Mixin, db.Model):
    __tablename__ = "armorandshieldtable"
# This table decides whether armor or shield is generated. Reference armor & shields (Table 2) in google sheets
# https://docs.google.com/spreadsheets/d/177MEAmvL87MidlJNoHbRtbEpbJRz5tBEtp8ZZef1ftw/edit#gid=0

    id = db.Column(db.Integer, unique=True, primary_key=True)
    encounterLevel = db.Column(db.Integer, nullable=False)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    moderateMinPercentage = db.Column(db.Integer)
    moderateMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    result = db.Column(db.String) # Result is armor or shield with bonus of up to +5 and special ability(s) up to +5
    itemBasePrice = db.Column(db.Integer) #Price of Magic 
    
