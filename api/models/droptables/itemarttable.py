from api.core import Mixin
from ..base import db


class ItemArtTable(Mixin, db.Model):
    __tablename__ = "arttable"
# For determining quantities and quality of art items found as part of hoard

    id = db.Column(db.Integer, unique=True, primary_key=True)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)

    
