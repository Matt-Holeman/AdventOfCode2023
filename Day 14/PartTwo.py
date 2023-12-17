import time

TOTAL_CYCLES = 1000 # This worked

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    platformList = rotateBoard(consumeFile(file), 'CCW')
    direction = 3
    for _ in range(TOTAL_CYCLES):
        for _ in range(4):
            platformList = rotateBoard(tiltBoard(platformList), 'CW')
            direction = (direction + 1) % 4
    printBoard(rotateBoard(platformList, 'CW'))
    print(f"Score: {scoreBoard(platformList, direction)}")

def consumeFile(file):
    platformList = []
    for line in file:
        platformList.append(line.strip())
    return(platformList)    

def rotateBoard(platformList, mode):
    platformListRotated = []
    if mode == 'CCW':
        for i in range(len(platformList)):
            platformListRotated.append("".join([row[len(platformList)-1-i] for row in platformList]))
    elif mode == 'CW':
        for i in range(len(platformList)):
            platformListRotated.append("".join([row[i] for row in platformList[::-1]]))
    else:
        raise ValueError(f"Invalid rotation mode.")
    return platformListRotated

def tiltBoard(platformList):
    outList = []
    for row in platformList:
        for _ in range(len(row) - len(row.replace('O',''))):
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

def scoreBoard(platformList, direction):
    score = 0
    platformListRotated = list(platformList)
    for _ in range(3 - direction):
        platformListRotated = rotateBoard(platformListRotated, 'CW')
    for row in platformListRotated:
        for cIdx in range(len(row)):
            c = row[cIdx]
            if c == 'O':
                score += (len(row) - cIdx)
    return score

def printBoard(platformList):
    for row in platformList:
        for c in row:
            print(f"{c} ", end="")
        print()

if __name__ == "__main__":
    main()