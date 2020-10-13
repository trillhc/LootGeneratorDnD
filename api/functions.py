import random
from api.models import db, ItemMagicChance, CoinGen, ArtGemChance, ItemTypeTable, ItemGemTable, MundaneItem, ArmorGeneration, MagicItemTable, ItemArtTable

from api.constants import *

def roll(input="1d100"):
    split = input.split("d")
    numberOfDice = int(split[0])
    maxRoll = int(split[1])
    output = 0
    while numberOfDice>0:
        output = output + random.randint(1,maxRoll)
        numberOfDice = numberOfDice - 1
    return output


def generateLoot(settings=defaultLootRequest):
    result = []
    hoardNumber = 0
    for eachHoard in settings["hoards"]:
        print("1")
        result.append({
        "coins": 0,
        "gems": [],
        "art": [],
        "items": []
        })
        print("2")
        #coin gen
        coinRoll = roll()
        print("5")
        coinQ = CoinGen.query.filter(CoinGen.minPercentage <= coinRoll, CoinGen.maxPercentage >= coinRoll,
                                 CoinGen.level == eachHoard["level"]).first()
        print("4")
        parse = coinQ.result.split("x")
        totalCoins = roll(parse[0])*int(parse[1])*int(eachHoard["coins"])
        result[hoardNumber]["coins"] = result[hoardNumber]["coins"] + totalCoins

        #art and gem generation and value
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
                #use class to roll again for specific item and add that to the item dict (8 items)
                if mundaneQ.result == "alchemical":
                    mundaneAlchemical = roll()
                    mundaneQ = MundaneItem.query.filter(MundaneItem.minPercentage <= mundaneAlchemical, MundaneItem.itemClass == "alchemical",
                                                            MundaneItem.maxPercentage >= mundaneAlchemical).first()
                    newItems[eachNewItem]["name"] = mundaneQ.itemName          
                               

        result[hoardNumber]["items"] = result[hoardNumber]["items"] + newItems
        hoardNumber= hoardNumber + 1
    return result
