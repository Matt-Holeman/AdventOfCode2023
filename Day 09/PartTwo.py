def main():
    file = open("input.txt")
    historyList = consumeFile(file)
    total = 0
    for history in historyList:
        total += evaluateHistory(history)
    print(total)

def consumeFile(file):
    historyList = []
    for line in file:
        historyList.append([int(x) for x in line.split(' ')])
    return historyList

def evaluateHistory(layer):
    if all(x == 0 for x in layer):
        return layer[0]
    else:
        nextLayer = []
        for x in range(len(layer) - 1):
            nextLayer.append(layer[x+1] - layer[x])
        return layer[0] - evaluateHistory(nextLayer)

if __name__ == "__main__":
    main()