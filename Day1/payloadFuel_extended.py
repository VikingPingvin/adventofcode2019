import os
from Day1.payloadFuel import readSource
from Day1.payloadFuel import calcFuel

def calcExtendedFuel(moduleMass):
    totalFuel = 0
    additionalFuel = moduleMass
    while additionalFuel > 0:
        additionalFuel = calcFuel(additionalFuel)
        if additionalFuel <=0:
            break
        totalFuel += additionalFuel
    return totalFuel

if __name__ == "__main__":
    #sourceLocation = os.path.join(os.path.dirname(__file__), 'source.txt')
    moduleMasses = readSource("source")
    fuelList = []
    for moduleMass in moduleMasses:
        fuelList.append(calcExtendedFuel(moduleMass))
    print(sum(fuelList))
