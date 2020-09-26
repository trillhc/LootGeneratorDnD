from api.core import Mixin
from .base import db


class ShieldTypeGeneration(Mixin, db.Model):
    __tablename__ = "shieldtypetable"
# This table generates type of shield, reference randomshieldtype (Table 4) in google sheets
# https://docs.google.com/spreadsheets/d/19AtJAPoJwQ5SkND8xWPy-sUWymMjrH6zaNybFoD0iQs/edit#gid=0

    id = db.Column(db.Integer, unique=True, primary_key=True)
    encounterLevel = db.Column(db.Integer, nullable=False)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)
    
