from sys import setrecursionlimit
import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    mirrorMatrix = consumeFile(file)
    stepHistory = {}
    travel(mirrorMatrix, stepHistory, 0, 0, 1, 0)
    visualiseStepHistory(stepHistory, mirrorMatrix)
    print(len(stepHistory.keys()))

def consumeFile(file):
    outMatrix = []
    for line in file:
        outMatrix.append([c for c in line.strip()])
    return outMatrix

def travel(mirrorMatrix, stepHistory, xPos, yPos, xIncremenet, yIncrement):
    newPath = False
    while True:
        if yPos >= len(mirrorMatrix) or yPos < 0 or xPos >= len(mirrorMatrix[yPos]) or xPos < 0:
            break
        c = mirrorMatrix[yPos][xPos]

        if (xPos,yPos) in stepHistory:
            stepHistory[(xPos, yPos)] += 1
        else:
            stepHistory[(xPos, yPos)] = 1
            newPath = True
        if c == '-' and yIncrement != 0:
            if not newPath:
                break
            travel(mirrorMatrix, stepHistory, xPos, yPos, -1, 0)
            travel(mirrorMatrix, stepHistory, xPos, yPos, 1, 0)
            break
        if c == '|' and xIncremenet != 0:
            if not newPath:
                break
            travel(mirrorMatrix, stepHistory, xPos, yPos, 0, -1)
            travel(mirrorMatrix, stepHistory, xPos, yPos, 0, 1)
            break
        elif c == '/':
            xIncremenet, yIncrement = 0-yIncrement, 0-xIncremenet
        elif c == '\\':
            xIncremenet, yIncrement = yIncrement, xIncremenet
        xPos += xIncremenet
        yPos += yIncrement
    return stepHistory

def visualiseStepHistory(stepHistory, mirrorMatrix):
    print()
    for y in range(len(mirrorMatrix)):
        for x in range(len(mirrorMatrix)):
            if (x,y) in stepHistory:
                c = mirrorMatrix[y][x]
                c = '#' if c == '.' else c
                print(c,end="")
            else:
                print('.',end="")
        print()        

if __name__ == "__main__":
    main()