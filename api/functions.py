import random
from api.models import db, Person, Email, CoinGen
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
        "coins": 0
    }
    for eachHoard in settings["hoards"]:
        r = roll()
        q = CoinGen.query.filter(CoinGen.minpercentage <= r, CoinGen.maxpercentage >= r,
                                 CoinGen.level == eachHoard["level"]).first()
        parse = q.result.split("x")
        totalCoins = roll(parse[0])*parse[1]*eachHoard["coins"]
        result["coins"] = result["coins"] + totalCoins
    return result
