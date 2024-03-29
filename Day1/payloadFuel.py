from math import floor


def calcFuel(mass):
    fuel = floor(mass / 3) - 2
    # print("asd")
    return fuel


def readSource(path):
    masses = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            masses.append(int(line.strip('\n')))
        return masses


if __name__ == "__main__":
    masses = readSource("source")
    fuelAmount = 0
    for mass in masses:
        fuelAmount += calcFuel(mass)
    print(fuelAmount)
