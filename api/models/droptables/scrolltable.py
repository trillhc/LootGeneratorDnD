from api.core import Mixin
from ..base import db


class scrollTable(Mixin, db.Model):
    __tablename__ = "scrolltable"
# For Scrolls, or other One-Time Use Spell Trigger Items
    id = db.Column(db.Integer, unique=True, primary_key=True)
    itemMinPercent = db.Column(db.Integer)
    itemMaxPercent = db.Column(db.Integer)
    result = db.Column(db.String)
    itemCost = db.Column(db.Integer)
    spellLevel = db.Column(db.Integer) # Level of Spell
    magicSource = db.Column(db.String) # Arcane or Divine (or neither for Artificers)
        