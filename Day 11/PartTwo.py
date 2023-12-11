SPACE_SHIFT = 1000000

def main():
    file = open("input.txt")
    galaxyList = shiftEmptySpace(consumeFile(file))
    calculateSumShortestPaths(galaxyList)

def consumeFile(file):
    galaxyList = []
    y = 0
    for line in file:
        x = 0
        for c in line:
            if c == '#':
                galaxyList.append([x,y])
            x += 1
        y += 1
    return galaxyList

def shiftEmptySpace(galaxyList):    
    for plane in [0,1]:
        coords = [g[plane] for g in galaxyList]
        emptySpace = []
        for i in range(140):
            if i not in coords:
                emptySpace.append(i)
        for empty in emptySpace:
            for idx in range(len(galaxyList)):
                if galaxyList[idx][plane] > empty:
                    galaxyList[idx][plane] += (SPACE_SHIFT - 1)
            for idx in range(len(emptySpace)):
                if emptySpace[idx] > empty:
                    emptySpace[idx] += (SPACE_SHIFT - 1)
    return galaxyList

def calculateSumShortestPaths(galaxyList):
    sum = 0
    for idx in range(len(galaxyList)):
        g1 = galaxyList[idx]
        for g2 in galaxyList[idx+1:]:
            sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print(sum)

if __name__ == "__main__":
    main()