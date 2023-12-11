import sys

def main():
    file = open("input.txt")
    sys.setrecursionlimit(5000)
    traversePipes(consumeFile(file))

def consumeFile(file):
    pipeMatrix = []
    for line in file:
        pipeMatrix.append(list(line.strip()))
    return pipeMatrix

def traversePipes(pipeMatrix):
    oldX, oldY = findStartingPosition(pipeMatrix)
    x, y = oldX, oldY+1
    c = 0
    found = False
    while not found:
        c += 1
        x, y, oldX, oldY, found = findNextDirection((x, y), (oldX, oldY), pipeMatrix)
    print(c/2)

def findStartingPosition(pipeMatrix):
    for y in range(len(pipeMatrix)):
        row = pipeMatrix[y]
        for x in range(len(row)):
            cell = row[x]
            if cell == 'S':
                return (x+1, y)
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


if __name__ == "__main__":
    main()