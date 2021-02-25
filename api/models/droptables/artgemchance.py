from api.core import Mixin
from ..base import db


class ArtGemChance(Mixin, db.Model):
    __tablename__ = "artgemchance"
    # For determining if you get art or gems and how many

    id = db.Column(db.Integer, unique=True, primary_key=True)
    encounterLevel = db.Column(db.Integer, nullable=True)
    minPercentage = db.Column(db.Integer, nullable=False)
    maxPercentage = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)
    artOrGem = db.Column(db.String)

