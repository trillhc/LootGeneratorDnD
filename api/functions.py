import random
from api.models import *
from  sqlalchemy.sql.expression import func, select
from api.constants import *
import sys
import os

def roll(input="1d100"):
    split = input.split("d")
    if len(split)<2:
        return int(input)
    numberOfDice = int(split[0])
    maxRoll = int(split[1])
    output = 0
    while numberOfDice>0:
        output = output + random.randint(1,maxRoll)
        numberOfDice = numberOfDice - 1
    #print("rolled "+str(output))
    return output


def generateLoot(settings=defaultLootRequest):
    result = []
    hoardNumber = 0
    for eachHoard in settings["hoards"]:
            result.append({
                "coins": 0,
                "gems": {"list": [],
                         "total": 0},
                "art": {"list": [],
                        "total": 0},
                "items": []
            })
            for enemy in range(1,int(settings["hoards"][hoardNumber]["quantity"])):
                try:
                    #coin gen
                    try:
                        coinRoll = roll()
                        coinQ = CoinGen.query.filter(CoinGen.minPercentage <= coinRoll, CoinGen.maxPercentage >= coinRoll,
                                                 CoinGen.level == eachHoard["level"]).first()
                        totalCoins = 0
                        if coinQ.result != "0":
                            parse = coinQ.result.split("x")
                            totalCoins = roll(parse[0])*int(parse[1])*int(eachHoard["coins"])
                            result[hoardNumber]["coins"] = result[hoardNumber]["coins"] + totalCoins
                    except Exception as e:
                        print("Coin Gen Error")
                        print(str(e))
                    #art and gem generation and value
                    try:
                        chanceRoll = roll()
                        chanceQ = ArtGemChance.query.filter(ArtGemChance.minPercentage <= chanceRoll, ArtGemChance.maxPercentage >= chanceRoll,
                                                 ArtGemChance.encounterLevel == eachHoard["level"]).first()
                        if chanceQ.artOrGem=="art":
                            amountOfNewArt = roll(chanceQ.result)
                            newArt = []
                            artTotal = 0
                            for eachNewArt in range(0,amountOfNewArt):
                                r = roll()
                                q = ItemArtTable.query.filter(ItemArtTable.minPercentage <= r, ItemArtTable.maxPercentage >= r).first()
                                artParse = q.result.split("x")
                                artValue = roll(artParse[0])*int(artParse[1])
                                newArt = newArt + [artValue]
                                artTotal = artTotal + artValue
                            result[hoardNumber]["art"]["list"] = result[hoardNumber]["art"]["list"] + newArt
                            result[hoardNumber]["art"]["total"] = result[hoardNumber]["art"]["total"] + artTotal
                            result[hoardNumber]["art"]["quantity"] = amountOfNewArt

                        if chanceQ.artOrGem=="gem":
                            amountOfNewGems = roll(chanceQ.result)
                            newGems = []
                            gemTotal = 0
                            for eachNewGem in range(0,amountOfNewGems):
                                r = roll()
                                q = ItemGemTable.query.filter(ItemGemTable.minPercentage <= r, ItemGemTable.maxPercentage >= r).first()
                                gemParse = q.result.split("x")
                                gemValue = roll(gemParse[0])*int(gemParse[1])
                                newGems = newGems + [gemValue]
                                gemTotal = gemTotal + gemValue
                            result[hoardNumber]["gems"]["list"] = result[hoardNumber]["gems"]["list"] + newGems
                            result[hoardNumber]["gems"]["total"] = gemTotal
                            result[hoardNumber]["gems"]["quantity"] = amountOfNewGems
                    except Exception as e:
                        print("Art or Gem Error")
                        print(str(e))
                    #determine amount of mundane,minor,medium,major itmes
                    itemMagicalnessRoll = roll()
                    newItems = []
                    magicalnessQ = ItemMagicChance.query.filter(ItemMagicChance.encounterLevel == settings["hoards"][hoardNumber]["level"],
                                                                ItemMagicChance.minPercentage <= itemMagicalnessRoll, ItemMagicChance.maxPercentage >= itemMagicalnessRoll).first()
                    amountOfNewItems = roll(magicalnessQ.result)
                    for eachNewItem in range(0, amountOfNewItems):
                        newItems = newItems + [{
                            "magicalness": magicalnessQ.magicalness
                        }]
                        if magicalnessQ.magicalness=="mundane":
                            #for eachNewItem in range(0, amountOfNewItems):
                            mundaneRoll = roll()
                            mundaneQ = MundaneItem.query.filter(MundaneItem.minPercentage <= mundaneRoll, MundaneItem.itemClass == "init",
                                                                        MundaneItem.maxPercentage >= mundaneRoll).first()
                            loops = 0
                            while mundaneQ.superCategory == True and loops < 20:
                                mundaneCat = roll()
                                #mundaneQ = MundaneItem.query.filter(MundaneItem.itemClass == mundaneQ.result).order_by(func.random()).limit(1).first()
                                mundaneQ = MundaneItem.query.filter(MundaneItem.minPercentage <= mundaneCat,
                                                                    MundaneItem.itemClass == mundaneQ.result,
                                                                    MundaneItem.maxPercentage >= mundaneCat).first()
                                loops = loops + 1
                            newItems[eachNewItem]["name"] = mundaneQ.itemName
                            newItems[eachNewItem]["quantity"] = roll(mundaneQ.result)
                        else:
                            #for eachNewItem in range(0, amountOfNewItems):
                            godRoll = roll()
                            godQ = ItemMagicGod.query.filter(getattr(ItemMagicGod, magicalnessQ.magicalness+"MinPercentage") <= godRoll,
                                                                        getattr(ItemMagicGod, magicalnessQ.magicalness+"MaxPercentage") >= godRoll).first()
                            print(godQ.result)
                            if godQ.result=="weapon" or godQ.result=="armorShield":
                                addAbilities = 0
                                abilityBonus = 0
                                itemRoll = roll()
                                itemQ = EnchantBase.query.filter(
                                    getattr(EnchantBase, magicalnessQ.magicalness + "MinPercentage") <= itemRoll,
                                    getattr(EnchantBase, magicalnessQ.magicalness + "MaxPercentage") >= itemRoll,
                                    EnchantBase.category=="init",
                                    EnchantBase.type==godQ.result).first()
                                while itemQ.result=="specialAbilityRR":
                                    addAbilities = addAbilities + 1
                                    itemRoll = roll()
                                    itemQ = EnchantBase.query.filter(
                                        getattr(EnchantBase, magicalnessQ.magicalness + "MinPercentage") <= itemRoll,
                                        getattr(EnchantBase, magicalnessQ.magicalness + "MaxPercentage") >= itemRoll,
                                        EnchantBase.category == "init",
                                        EnchantBase.type == godQ.result).first()
                                if "specific" in itemQ.result:
                                    specificType = "weapon"
                                    if godQ.result=="armorShield":
                                        specificType = itemQ.result.split("specific")[1]
                                    itemRoll = roll()
                                    itemQ = SpecificItem.query.filter(
                                        getattr(SpecificItem, magicalnessQ.magicalness + "MinPercentage") <= itemRoll,
                                        getattr(SpecificItem, magicalnessQ.magicalness + "MaxPercentage") >= itemRoll,
                                        SpecificItem.category == specificType).first()
                                    newItems[eachNewItem]["name"] = itemQ.name
                                    newItems[eachNewItem]["price"] = itemQ.price
                                    newItems[eachNewItem]["type"] = itemQ.category
                                else:
                                    abilityBonus = itemQ.abilityBonus
                                    itemType = itemQ.result
                                    while itemQ.superCategory is True:
                                        itemRoll = roll()
                                        trying = itemQ.result
                                        itemQ = EnchantBase.query.filter(
                                            getattr(EnchantBase, magicalnessQ.magicalness + "MinPercentage") <= itemRoll,
                                            getattr(EnchantBase, magicalnessQ.magicalness + "MaxPercentage") >= itemRoll,
                                            EnchantBase.category == trying,
                                            EnchantBase.type == itemType).first()
                                    if itemQ.category == "ranged":
                                        itemType = "ranged"
                                    loops = 0
                                    newItems[eachNewItem]["abilities"] = []
                                    abilityMax = abilityBonus
                                    while addAbilities > 0 and loops < 5:
                                        loops = loops + 1
                                        addAbilities = addAbilities - 1
                                        abilityRoll = roll()
                                        abilityQ = ItemTypeTable.query.filter(
                                            getattr(ItemTypeTable, magicalnessQ.magicalness + "MinPercentage") <= abilityRoll,
                                            getattr(ItemTypeTable, magicalnessQ.magicalness + "MaxPercentage") >= abilityRoll,
                                            ItemTypeTable.itemEnchantType==itemType,
                                        ).first()
                                        if abilityQ.result=="extraAbility":
                                            addAbilities = addAbilities + 2
                                        elif abilityMax+abilityQ.abilityPlus <= 10:
                                            newItems[eachNewItem]["abilities"] = newItems[eachNewItem]["abilities"] + [abilityQ.result]
                                            abilityMax = abilityMax + abilityQ.abilityPlus
                                    newItems[eachNewItem]["name"] = itemQ.result
                                    newItems[eachNewItem]["price"] = itemQ.price
                                    newItems[eachNewItem]["abilityBonus"] = abilityBonus
                                    newItems[eachNewItem]["type"] = itemType
                            #potion gen
                            elif godQ.result=="potion":
                                potionRoll = roll()
                                potionQ = PotionTable.query.filter(
                                    getattr(PotionTable, magicalnessQ.magicalness + "MinPercentage") <= potionRoll,
                                    getattr(PotionTable, magicalnessQ.magicalness + "MaxPercentage") >= potionRoll,
                                ).first()
                                newItems[eachNewItem]["type"] = "potion"
                                newItems[eachNewItem]["name"] = potionQ.result
                                newItems[eachNewItem]["price"] = potionQ.price
                            #rod ring staff wand gen
                            elif godQ.result=="rod" or godQ.result=="ring" or godQ.result=="staff" or godQ.result=="wand":
                                trinketRoll = roll()
                                trinketQ = MagicItemTable.query.filter(
                                    getattr(MagicItemTable, magicalnessQ.magicalness + "MinPercentage") <= trinketRoll,
                                    getattr(MagicItemTable, magicalnessQ.magicalness + "MaxPercentage") >= trinketRoll,
                                    MagicItemTable.itemType==godQ.result,
                                ).first()
                                newItems[eachNewItem]["type"] = godQ.result
                                newItems[eachNewItem]["name"] = trinketQ.result
                                newItems[eachNewItem]["price"] = trinketQ.price
                            elif godQ.result=="wonderous":
                                wonderRoll = roll()
                                wonderQ = WonderousItemTable.query.filter(
                                    WonderousItemTable.itemMinPercent <= wonderRoll,
                                    WonderousItemTable.itemMaxPercent >= wonderRoll,
                                    WonderousItemTable.itemQuality == magicalnessQ.magicalness
                                ).first()
                                newItems[eachNewItem]["type"] = "wonderous"
                                newItems[eachNewItem]["name"] = wonderQ.result
                                newItems[eachNewItem]["price"] = wonderQ.price
                            #scroll gen
                            elif godQ.result=="scroll":
                                sourceRoll = roll()
                                if sourceRoll > 70:
                                    magicSource = "arcane"
                                else:
                                    magicSource = "divine"
                                if magicalnessQ.magicalness == "minor":
                                    uses = roll("1d3")
                                elif magicalnessQ.magicalness == "medium":
                                    uses = roll("1d4")
                                else:
                                    uses = roll("1d6")
                                scrollGenRoll = roll()
                                scrollGenQ = ScrollGeneration.query.filter(
                                    getattr(ScrollGeneration, magicalnessQ.magicalness + "MinPercentage") <= scrollGenRoll,
                                    getattr(ScrollGeneration, magicalnessQ.magicalness + "MaxPercentage") >= scrollGenRoll,
                                ).first()
                                scrollRoll = roll()
                                scrollQ = ScrollTable.query.filter(
                                    ScrollTable.itemMinPercent <= scrollRoll,
                                    ScrollTable.itemMaxPercent >= scrollRoll,
                                    ScrollTable.magicSource == magicSource,
                                    ScrollTable.spellLevel == scrollGenQ.spellLevel,
                                ).first()
                                newItems[eachNewItem]["name"] = scrollQ.result
                                newItems[eachNewItem]["amount"] = uses
                                newItems[eachNewItem]["type"] = "scroll"
                                newItems[eachNewItem]["spell"] = scrollGenQ.spellLevel
                                newItems[eachNewItem]["caster"] = scrollGenQ.spellCasterLevel
                                newItems[eachNewItem]["price"] = scrollQ.price
                                newItems[eachNewItem]["magicSource"] = magicSource
                    result[hoardNumber]["items"] = result[hoardNumber]["items"] + newItems

                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            hoardNumber = hoardNumber + 1

    
    return result


'''
if ItemTypeTable(result = scroll):
    for eachNewScroll in range(0, amountOfNewScrolls):
        scrolltype = roll()   # should be either arcane or divine
            if roll() <= 71 : 
                scrolltype = "divine"
            else 
                scrolltype = "arcane"
'''