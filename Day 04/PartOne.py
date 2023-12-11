
def main():
    evaluateScore(consumeFile("input.txt"))

def consumeFile(filename):
    file = open(filename)
    count = 0
    outputDict = {}
    for line in file:
        line = line[line.index(':')+2:]
        line = line.replace('  ', ' ')
        splitString = line.split('|')
        winningNumbers = splitString[0].strip().split(' ')
        heldNumbers = splitString[1].strip().split(' ')
        outputDict[count] = [winningNumbers, heldNumbers]
        count += 1
    return outputDict

def evaluateScore(cardDict):
    totalScore = 0
    for i in cardDict.keys():
        print(f"=== {i+1} ===")
        cardScore = 0
        nextScore = 1
        card = cardDict[i]
        for n in card[1]:
            if n in card[0]:
                print(n)
                cardScore = nextScore
                nextScore *= 2
        totalScore += cardScore
    print(f"Total: {totalScore}")
    return totalScore

if __name__ == "__main__":
    main()