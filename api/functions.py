import random
from api.models import db, CoinGen, ItemTypeTable, ItemGemTable, MundaneItem, ArmorGeneration, MagicItemTable, ItemArtTable
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
    result = {
        "coins": 0,
        "gems": [],
        "art": []
    }
    #coin gen
    for eachHoard in settings["hoards"]:
        r = roll()
        q = CoinGen.query.filter(CoinGen.minPercentage <= r, CoinGen.maxPercentage >= r,
                                 CoinGen.level == eachHoard["level"]).first()
        parse = q.result.split("x")
        totalCoins = roll(parse[0])*parse[1]*eachHoard["coins"]
        result["coins"] = result["coins"] + totalCoins
    #art gen
    for eachHoard in settings["hoards"]:
        r = roll()
        q = ItemArtTable.query.filter(ItemArtTable.minPercentage <= r, ItemArtTable.maxPercentage >= r,
                                 ItemArtTable.level == eachHoard["level"], ItemArtTable.value==False).first()
        newArt = []
        amountOfNewArt = roll(q.result)
        for eachNewArt in range(0,amountOfNewArt):
            r = roll()
            q = ItemArtTable.query.filter(ItemArtTable.minPercentage <= r, ItemArtTable.maxPercentage >= r,
                                           ItemArtTable.value == True).first()
            newArt = newArt + [q.result]
        result["art"] = result["art"] + newArt
    #gem gen
    for eachHoard in settings["hoards"]:
        r = roll()
        q = ItemGemTable.query.filter(ItemGemTable.minPercentage <= r, ItemGemTable.maxPercentage >= r,
                                 ItemGemTable.level == eachHoard["level"], ItemGemTable.value==False).first()
        newGems = []
        amountOfNewGems = roll(q.result)
        for eachNewArt in range(0,amountOfNewGems):
            r = roll()
            q = ItemGemTable.query.filter(ItemGemTable.minPercentage <= r, ItemGemTable.maxPercentage >= r,
                                           ItemGemTable.value == True).first()
            newGems = newGems + [q.result]
        result["gems"] = result["gems"] + newGems
    return result
