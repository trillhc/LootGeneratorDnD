import random
from api.models import db, EnchantBase, SpecialAbility, ItemMagicChance, SpecificItem, EnchantableItem, CoinGen, ArtGemChance, ItemMagicGod, ItemGemTable, MundaneItem, ArmorGeneration, MagicItemTable, ItemArtTable
from  sqlalchemy.sql.expression import func, select
from api.constants import *

def roll(input="1d100"):
    split = input.split("d")
    numberOfDice = int(split[0])
    maxRoll = int(split[1])
    output = 0
    while numberOfDice>0:
        output = output + random.randint(1,maxRoll)
        numberOfDice = numberOfDice - 1
    print("rolled "+str(output))
    return output


def generateLoot(settings=defaultLootRequest):
    result = []
    hoardNumber = 0
    for eachHoard in settings["hoards"]:
        try:
            result.append({
            "coins": 0,
            "gems": [],
            "art": [],
            "items": []
            })
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
                    for eachNewArt in range(0,amountOfNewArt):
                        r = roll()
                        q = ItemArtTable.query.filter(ItemArtTable.minPercentage <= r, ItemArtTable.maxPercentage >= r).first()
                        artParse = q.result.split("x")
                        newArt = newArt + [roll(artParse[0])*int(artParse[1])]
                    result[hoardNumber]["art"] = result[hoardNumber]["art"] + newArt
                if chanceQ.artOrGem=="gem":
                    amountOfNewGems = roll(chanceQ.result)
                    newGems = []
                    for eachNewArt in range(0,amountOfNewGems):
                        r = roll()
                        q = ItemGemTable.query.filter(ItemGemTable.minPercentage <= r, ItemGemTable.maxPercentage >= r).first()
                        gemParse = q.result.split("x")
                        newGems = newGems + [roll(gemParse[0])*int(gemParse[1])]
                    result[hoardNumber]["gems"] = result[hoardNumber]["gems"] + newGems
            except Exception as e:
                print("Art or Gem Error")
                print(str(e))
            #determine amount of mundane,minor,medium,major itmes
            itemMagicalnessRoll = roll()
            newItems = []
            magicalnessQ = ItemMagicChance.query.filter(ItemMagicChance.minPercentage <= itemMagicalnessRoll, ItemMagicChance.maxPercentage >= itemMagicalnessRoll).first()
            amountOfNewItems = roll(magicalnessQ.result)
            for eachNewItem in range(0, amountOfNewItems):
                newItems = newItems + [{
                    "magicalness": magicalnessQ.magicalness
                }]
            if magicalnessQ.magicalness=="mundane":
                for eachNewItem in range(0, amountOfNewItems):
                    mundaneRoll = roll()
                    mundaneQ = MundaneItem.query.filter(MundaneItem.minPercentage <= mundaneRoll, MundaneItem.itemClass == "init",
                                                                MundaneItem.maxPercentage >= mundaneRoll).first()
                    loops = 0
                    print(mundaneQ.result)
                    while mundaneQ.supercategory == True and loops < 20:
                        print(str(loops))
                        mundaneCat = roll()
                        #broken
                        mundaneQ = MundaneItem.query.filter(MundaneItem.itemClass == mundaneQ.result).order_by(func.random()).limit(1).first()
                        print(mundaneQ.itemName)
                        loops = loops + 1
                    newItems[eachNewItem]["name"] = mundaneQ.itemName
            else:
                pass
                '''
                for eachNewItem in range(0, amountOfNewItems):
                        godRoll = roll()
                        godQ = ItemMagicGod.query.filter(getattr(ItemMagicGod, magicalnessQ.magicalness+"MinPercentage") <= godRoll,
                                                                    getattr(ItemMagicGod, magicalnessQ.magicalness+"MaxPercentage") >= godRoll).first()
                        if godQ.result=="weapon":
                            weaponRoll = roll()
                            weaponQ = EnchantableItem.query.filter(
                                getattr(EnchantableItem, magicalnessQ.magicalness + "MinPercentage") <= weaponRoll,
                                getattr(EnchantableItem, magicalnessQ.magicalness + "MaxPercentage") >= weaponRoll,
                                EnchantableItem.category=="weapon").first()
                            if weaponQ.result=="specific":
                                weaponQ = SpecificItem.query.filter(
                                    getattr(SpecificItem, magicalnessQ.magicalness + "MinPercentage") <= weaponRoll,
                                    getattr(SpecificItem, magicalnessQ.magicalness + "MaxPercentage") >= weaponRoll,
                                    SpecificItem.category == "weapon").first()
                            weapontypeRoll = roll()
                            weapontypeQ = EnchantBase.query.filter(EnchantBase.minPercentage <= weapontypeRoll,
                                                                   EnchantBase.category=="weapontype",
                                                                   EnchantBase.maxPercentage >= weapontypeRoll).first()
                            weapontypeQ = EnchantBase.query.filter(EnchantBase.minPercentage <= weapontypeRoll,
                                                                   EnchantBase.category=="weapontype",
                                                                   EnchantBase.maxPercentage >= weapontypeRoll).first()
                            if weaponQ.result == "specific":
                                pass
                            newItems[eachNewItem]["name"] = weaponQ.name
                            newItems[eachNewItem]["price"] = weaponQ.price
                '''
            result[hoardNumber]["items"] = result[hoardNumber]["items"] + newItems

        except Exception as e:
            print(str(e))
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