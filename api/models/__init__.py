# this file structure follows http://flask.pocoo.org/docs/1.0/patterns/appfactories/
# initializing db in api.models.base instead of in api.__init__.py
# to prevent circular dependencies
from .droptables.itemarttable import ItemArtTable
from .droptables.itemgemtable import ItemGemTable
from .droptables.god import ItemMagicGod
from .droptables.artgemchance import ArtGemChance
from .droptables.specialability import SpecialAbility
from .droptables.specificitem import SpecificItem
from .droptables.itemmagicchance import ItemMagicChance
from .droptables.enchantableitems import EnchantableItem
from .droptables.magicitem import MagicItemTable
from .droptables.mundaneitems import MundaneItem
from .droptables.itemgeneration.armortable import ArmorGeneration
from .droptables.itemgeneration.weapontable import WeaponTable
from .droptables.coinGen import CoinGen
from .droptables.enchantbase import EnchantBase
from .droptables.itemtypetable import ItemTypeTable
from .droptables.specificitem import SpecificItem
from .droptables.potionTable import PotionTable
from .droptables.wonderousitem import WonderousItemTable
from .droptables.scrolltable import ScrollTable

from .base import db

__all__ = ["Email", "Person", "db", "CoinGen", "ItemMagicGod", "ItemArtTable", "EnchantBase", "ItemGemTable", "ArtGemChance",
           "SpecialAbility", "SpecificItem", "ItemMagicChance", "EnchantableItem", "MagicItemTable", "MundaneItem", "ArmorGeneration",
           "WeaponTable", "ItemTypeTable", "PotionTable", "WonderousItemTable", "ScrollTable"]

# You must import all of the new Models you create to this page
