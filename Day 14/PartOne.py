import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    platformList = tiltBoard(consumeFile(file))
    scoreBoard(platformList)

def consumeFile(file):
    platformListRotated = []
    platformList = []
    for line in file:
        platformList.append(line.strip())

    # Rotating so we're only needing to evaluate a single row at a time (tilt left rather than up)
    for i in range(len(platformList)):
        platformListRotated.append("".join([row[len(platformList)-1-i] for row in platformList]))
    return platformListRotated

def tiltBoard(platformList):
    outList = []
    for row in platformList:
        count = len(row) - len(row.replace('O',''))
        for _ in range(count):
            lowestIndex = -1
            for cIdx in range(len(row)):
                c = row[cIdx]
                if c == 'O' and lowestIndex != -1:
                    row = row[:cIdx] + '.' + row[cIdx+1:]
                    row = row[:lowestIndex] + 'O' + row[lowestIndex+1:]
                    break
                elif c == '.' and lowestIndex == -1:
                    lowestIndex = cIdx
                elif c == '#':
                    lowestIndex = -1
        outList.append(row)
    return outList

def scoreBoard(platformList):
    score = 0
    for row in platformList:
        for cIdx in range(len(row)):
            c = row[cIdx]
            if c == 'O':
                score += (len(row) - cIdx)
    print(score)


if __name__ == "__main__":
    main()