from api.core import Mixin
from .base import db


class spellList(Mixin, db.Model):
    __tablename__ = "Spell List"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    spellName = db.Column(db.String, nullable=False)
    primarySchool = db.Column(db.String, nullable=False)
    priSubSchool = db.Column(db.Integer, nullable=False)
    secondarySchool = db.Column(db.Integer, nullable=False)
    secSubSchool = db.Column(db.Integer, nullable=False)
    tertiarySchool = db.Column(db.String, nullable=False)
    tertSubSchool = db.Column(db.String, nullable=False)
    bardSpellLevel = db.Column(db.Integer, nullable=False)
    clericSpellLevel = db.Column(db.Integer, nullable=False)
    domainSpellName = db.Column(db.String, nullable=False)
    domainSpellLevel = db.Column(db.String, nullable=False)
    druidSpellLevel = db.Column(db.Integer, nullable=False)
    paladinSpellLevel = db.Column(db.Integer, nullable=False)
    rangerSpellLevel = db.Column(db.Integer, nullable=False)
    sorcererSpellLevel = db.Column(db.Integer, nullable=False)
    wizardSpellLevel = db.Column(db.Integer, nullable=False)
    verbalSpellComponent = db.Column(db.String, nullable=False)
    somaticSpellComponent = db.Column(db.String, nullable=False)
    materialSpellComponent = db.Column(db.String, nullable=False)
    focusSpellComponent = db.Column(db.String, nullable=False)
    xpSpellComponent = db.Column(db.String, nullable=False)
    spellCastingTime = db.Column(db.String, nullable=False)
    spellRange = db.Column(db.String, nullable=False)
    spellArea = db.Column(db.String, nullable=False)
    spellTargets = db.Column(db.String, nullable=False)
    spellDuration = db.Column(db.String, nullable=False)
    spellSavingThrow = db.Column(db.String, nullable=False)
    spellResistance = db.Column(db.String, nullable=False)
    spellDescription = db.Column(db.String, nullable=False)

    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return f"<id {self.id}>"
