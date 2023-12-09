import json

def main():
    bagDict = consumeFile("input.txt")
    print(validateFile(bagDict))

def consumeFile(filename):
    file = open(filename)
    gameCount = 1
    bagDict = {}
    for game in file:
        gameDict = {}
        game = game[game.find(":"):]
        game = game.lstrip(": ")
        roundCount = 0
        for round in game.split(';'):
            roundDict = {}
            round = round.strip()
            for colour in round.split(","):
                colour = colour.strip()
                itemPair = colour.split(" ")
                roundDict[str(itemPair[1])] = int(itemPair[0])
            gameDict[roundCount] = roundDict
            roundCount += 1
        bagDict[gameCount] = gameDict
        gameCount += 1
    return bagDict

def validateFile(bagDict):
    sumPower = 0
    for gameID in bagDict.keys():
        highestRed = 0
        highestBlue = 0
        highestGreen = 0
        gameDict = bagDict[gameID]
        for roundID in gameDict:
            round = gameDict[roundID]
            if 'red' in round and round['red'] > highestRed:
                highestRed = round['red']
            if 'blue' in round and round['blue'] > highestBlue:
                highestBlue = round['blue']
            if 'green' in round and round['green'] > highestGreen:
                highestGreen = round['green']
        print(f"{gameID} - Red: {highestRed}, Blue: {highestBlue}, Green: {highestGreen} --> {highestRed * highestGreen * highestBlue}")
        sumPower += (highestRed * highestGreen * highestBlue)
    return sumPower
    




if __name__ == "__main__":
    main()