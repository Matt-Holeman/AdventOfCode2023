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
    successCount = 0
    for gameID in bagDict.keys():
        gamePass = True
        print(gameID)
        gameDict = bagDict[gameID]
        for roundID in gameDict:
            round = gameDict[roundID]
            if 'red' in round and round['red'] > 12:
                gamePass = False
                break
            elif 'green' in round and round['green'] > 13:
                gamePass = False
                break
            elif 'blue' in round and round['blue'] > 14:
                gamePass = False
                break
        if gamePass:
            successCount += gameID
    return successCount




if __name__ == "__main__":
    main()