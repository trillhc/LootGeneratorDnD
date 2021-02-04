from api.core import Mixin
from ..base import db


class ItemGemTable(Mixin, db.Model):
    __tablename__ = "gemtable"
# For determining quantities and quality of gems and found as part of hoard

    id = db.Column(db.Integer, unique=True, primary_key=True)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)
    
