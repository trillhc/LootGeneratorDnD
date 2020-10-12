# this file structure follows http://flask.pocoo.org/docs/1.0/patterns/appfactories/
# initializing db in api.models.base instead of in api.__init__.py
# to prevent circular dependencies
from .Email import Email
from .Person import Person
from .droptables.itemarttable import ItemArtTable
from .droptables.itemgemtable import ItemGemTable
from .droptables.itemtypetable import ItemTypeTable
from .droptables.magicitem import MagicItemTable
from .droptables.mundaneItems import MundaneItem
from .droptables.itemgeneration.armortable import ArmorGeneration
from .droptables.itemgeneration.weapontable import WeaponTable
from .droptables.coinGen import CoinGen
from .base import db

#not used
__all__ = ["Email", "Person", "db"]

# You must import all of the new Models you create to this page
