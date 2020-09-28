from api.core import Mixin
from .base import db


class spellList(Mixin, db.Model):
    __tablename__ = "Spell List"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    spellName = db.Column(db.String, nullable=False)
    primarySchool = db.Column(db.String)  #A spell can have multiple schools and sub-schools
    priSubSchool = db.Column(db.Integer)
    secondarySchool = db.Column(db.Integer)
    secSubSchool = db.Column(db.Integer)
    tertiarySchool = db.Column(db.String)
    tertSubSchool = db.Column(db.String)
    bardSpellLevel = db.Column(db.Integer)
    clericSpellLevel = db.Column(db.Integer) # different classes have different levels for same spell
    domainSpellName = db.Column(db.String)
    domainSpellLevel = db.Column(db.String)
    druidSpellLevel = db.Column(db.Integer)
    paladinSpellLevel = db.Column(db.Integer)
    rangerSpellLevel = db.Column(db.Integer)
    sorcererSpellLevel = db.Column(db.Integer)
    wizardSpellLevel = db.Column(db.Integer)
    verbalSpellComponent = db.Column(db.String) # Components for the spell in question
    somaticSpellComponent = db.Column(db.String)
    materialSpellComponent = db.Column(db.String)
    focusSpellComponent = db.Column(db.String)
    xpSpellComponent = db.Column(db.String)
    spellCastingTime = db.Column(db.String)
    spellRange = db.Column(db.String)
    spellArea = db.Column(db.String)
    spellTargets = db.Column(db.String)
    spellDuration = db.Column(db.String)
    spellSavingThrow = db.Column(db.String)
    spellResistance = db.Column(db.String)
    spellDescription = db.Column(db.String)

    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return f"<id {self.id}>"
