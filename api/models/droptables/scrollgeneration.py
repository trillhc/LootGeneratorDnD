from api.core import Mixin
from ..base import db


class ScrollGeneration(Mixin, db.Model):
    __tablename__ = "scrollgeneration"
# For Generating Scrolls
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercentage = db.Column(db.Integer)
    minorMaxPercentage = db.Column(db.Integer)
    mediumMinPercentage = db.Column(db.Integer)
    mediumMaxPercentage = db.Column(db.Integer)
    majorMinPercentage = db.Column(db.Integer)
    majorMaxPercentage = db.Column(db.Integer)
    spellLevel = db.Column(db.Integer) # Level of Spell
    spellCasterLevel = db.Column(db.Integer) # Caster Lvl for spell (Double Spell Level minus 1 above 1st)
        