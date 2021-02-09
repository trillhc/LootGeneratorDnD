from api.core import Mixin
from ..base import db


class ScrollGeneration(Mixin, db.Model):
    __tablename__ = "scrollgeneration"
# For Generating Scrolls
    id = db.Column(db.Integer, unique=True, primary_key=True)
    minorMinPercent = db.Column(db.Integer)
    minorMaxPercent = db.Column(db.Integer)
    mediumMinPercent = db.Column(db.Integer)
    mediumMaxPercent = db.Column(db.Integer)
    majorMinPercent = db.Column(db.Integer)
    majorMaxPercent = db.Column(db.Integer)
    spellLevel = db.Column(db.Integer) # Level of Spell
    spellCasterLevel = db.Column(db.Integer) # Caster Lvl for spell (Double Spell Level minus 1 above 1st)
        