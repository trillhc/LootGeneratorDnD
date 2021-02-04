from api.core import Mixin
from ..base import db


class WonderousItemTable(Mixin, db.Model):
    __tablename__ = "wonderousitems"
# For wonderous items, and other miscellaneous
    id = db.Column(db.Integer, unique=True, primary_key=True)
    itemMinPercent = db.Column(db.Integer)
    itemMaxPercent = db.Column(db.Integer)
    result = db.Column(db.String)
    itemCost = db.Column(db.Integer)
    itemQuality = db.Column(db.String) # Minor Medium or Major Item