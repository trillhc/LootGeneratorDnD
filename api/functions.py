import random
from api.models import db, CoinGen, ArtGemChance, ItemTypeTable, ItemGemTable, MundaneItem, ArmorGeneration, MagicItemTable, ItemArtTable
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
    hoardNumber = 1
    for eachHoard in settings["hoards"]:
        result[hoardNumber] = {
        "coins": 0,
        "gems": [],
        "art": []
        }
        #coin gen
        coinRoll = roll()
        coinQ = CoinGen.query.filter(CoinGen.minPercentage <= coinRoll, CoinGen.maxPercentage >= coinRoll,
                                 CoinGen.level == eachHoard["level"]).first()
        parse = coinQ.result.split("x")
        totalCoins = roll(parse[0])*parse[1]*eachHoard["coins"]
        result[hoardNumber]["coins"] = result["coins"] + totalCoins
        #art and gem generation and value
        chanceRoll = roll()
        chanceQ = ArtGemChance.query.filter(ArtGemChance.minPercentage <= chanceRoll, ArtGemChance.maxPercentage >= chanceRoll,
                                 ArtGemChance.level == eachHoard["level"]).first()
        if chanceQ.artOrGem=="art":
            amountOfNewArt = roll(chanceQ.result)
            newArt = []
            for eachNewArt in range(0,amountOfNewArt):
                r = roll()
                q = ItemArtTable.query.filter(ItemArtTable.minPercentage <= r, ItemArtTable.maxPercentage >= r).first()
                newArt = newArt + [q.result]
            result["art"] = result["art"] + newArt
        if chanceQ.artOrGem=="gem":
            amountOfNewGems = roll(chanceQ.result)
            newGems = []
            for eachNewArt in range(0,amountOfNewGems):
                r = roll()
                q = ItemGemTable.query.filter(ItemGemTable.minPercentage <= r, ItemGemTable.maxPercentage >= r).first()
                newGems = newGems + [q.result]
            result["gems"] = result["gems"] + newGems
    return result
