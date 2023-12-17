import time

MAX_X = 140
MAX_Y = 140
sReplace = '|'

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    pipeMatrix = consumeFile(file)
    loopPipeList = traversePipes(pipeMatrix)
    count = 0

    for y in range(len(pipeMatrix)):
        row = pipeMatrix[y]
        for x in range(len(row)):
            c = pipeMatrix[y][x]
            if pipeMatrix[y][x] == 'S':
                pipeMatrix[y][x] = sReplace
            if (x, y) not in loopPipeList:
                pipeMatrix[y][x] = '+'

    for y in range(len(pipeMatrix)):
        row = pipeMatrix[y]
        for x in range(len(row)):
            c = pipeMatrix[y][x]
            if c == '+' and not isLocationInLoop((x,y), pipeMatrix):
                pipeMatrix[y][x] = ' '
            elif c == '+':
                count += 1

    printVisual(pipeMatrix)    
    print(count)

def consumeFile(file):
    pipeMatrix = []
    for line in file:
        pipeMatrix.append(list(line.strip()))
    return pipeMatrix

def traversePipes(pipeMatrix):
    oldX, oldY = findStartingPosition(pipeMatrix)
    x, y = oldX, oldY+1
    loopPipeList = [[oldX, oldY]]
    c = 0
    found = False
    while not found:
        c += 1
        loopPipeList.append((x, y))
        x, y, oldX, oldY, found = findNextDirection((x, y), (oldX, oldY), pipeMatrix)
    return loopPipeList

def findStartingPosition(pipeMatrix):
    for y in range(len(pipeMatrix)):
        row = pipeMatrix[y]
        for x in range(len(row)):
            cell = row[x]
            if cell == 'S':
                return (x, y)
    raise ValueError(f"Could not find 'S' starting location")

def findNextDirection(s, oldS, pipeMatrix):
    x, y = s
    oldX, oldY = oldS
    c = pipeMatrix[y][x]
    if c == 'S':
        return (x, y, oldX, oldY, True)
    elif c == '|':
        if oldY > y:
            y -= 1
        else:
            y += 1
    elif c == '-':
        if oldX > x:
            x -= 1
        else:
            x += 1
    elif c == 'L':
        if oldY < y:
            x += 1
        else:
            y -= 1
    elif c == 'J':
        if oldY < y:
            x -= 1
        else:
            y -= 1
    elif c == '7':
        if oldY > y:
            x -= 1
        else:
            y += 1
    elif c == 'F':
        if oldY > y:
            x += 1
        else:
            y += 1
    oldX, oldY = s
    return (x, y, oldX, oldY, False)

def isLocationInLoop(pipe, pipeMatrix):
    pipeX, pipeY = pipe
    c = 0
    pair = ''
    for x in range(pipeX, MAX_X):
        if pipeMatrix[pipeY][x] in '|':
            c += 1
        if pipeMatrix[pipeY][x] in 'F7JL':
            if pair != '':
                if pair == 'F':
                    if pipeMatrix[pipeY][x] == 'J':
                        c += 1
                    pair = ''
                if pair == 'L':
                    if pipeMatrix[pipeY][x] == '7':
                        c += 1
                    pair = ''
            else:
                pair = pipeMatrix[pipeY][x]
    return (c % 2 == 1)

def printVisual(pipeMatrix):
    for y in range(len(pipeMatrix)):
        row = pipeMatrix[y]
        for x in range(len(row)):
            c = pipeMatrix[y][x]
            if c == '|':
                print('│', end="")
            elif c == '-':
                print('─', end="")
            elif c == 'L':
                print('└', end="")
            elif c == 'J':
                print('┘', end="")
            elif c == '7':
                print('┐', end="")
            elif c == 'F':
                print('┌', end="")
            else:
                print(c,end="")
        print()
        
if __name__ == "__main__":
    main()