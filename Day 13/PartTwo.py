import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    islandList = consumeFile(file)
    score = 0
    
    for island in islandList:
        _, rowIdx = findRefectionRow(island, -1)
        _, colIdx = findReflectionColumn(island, -1)
        score += findNewReflection(island, 'row', rowIdx, colIdx)
        score += findNewReflection(island, 'col', rowIdx, colIdx)
    print(score)

def consumeFile(file):
    islandList = []
    island = []
    for line in file:
        if line.strip() == '':
            islandList.append(island)
            island = []
        else:
            island.append(line.strip())
    islandList.append(island)
    return islandList

def findNewReflection(oldIsland, mode, previousRowIdx, previousColIdx):
    island = list(oldIsland)
    for y in range(len(island)):
        for x in range(len(island[0])):
            c = island[y][x]
            newc = '.' if c == '#' else '#'
            island[y] = island[y][:x] + newc + island[y][x+1:]
            if mode == 'row':
                score, i = findRefectionRow(island, previousRowIdx) 
                if score != 0 and i != previousRowIdx:
                    island = list(oldIsland)
                    return score
            elif mode == 'col':
                score, i = findReflectionColumn(island, previousColIdx)
                if score != 0 and i != previousColIdx:
                    island = list(oldIsland)
                    return score
            island = list(oldIsland)
    return 0

def findRefectionRow(island, previousIdx):
    score = 0
    outIdx = -1
    for rowIdx in range(len(island)-1):
        if island[rowIdx] == island[rowIdx+1]:
            correct = True
            if rowIdx == previousIdx:
                correct = False
            for x in range(len(island)):
                if rowIdx+1+x >= len(island) or rowIdx-x < 0:
                    break
                if island[rowIdx-x] != island[rowIdx+1+x]:
                    correct = False
                    break
            if not correct:
                continue
            else:
                score += ((rowIdx+1) * 100)
                outIdx = rowIdx
    return score, outIdx

def findReflectionColumn(island, previousIdx):
    island = island[::-1]
    score = 0
    outIdx = -1
    for columnIdx in range(len(island[0])-1):
        if "".join([x[columnIdx] for x in island]) == "".join([x[columnIdx+1] for x in island]):
            correct = True
            if columnIdx == previousIdx:
                correct = False
            for x in range(len(island)):
                if columnIdx+1+x >= len(island[0]) or columnIdx-x < 0:
                    break
                columnBackwards = "".join([c[columnIdx-x] for c in island])
                columnForwards = "".join([c[columnIdx+1+x] for c in island]) 
                if columnBackwards != columnForwards:
                    correct = False
                    break
            if not correct:
                continue
            else:
                score += (columnIdx+1)
                outIdx = columnIdx
    return score, outIdx

if __name__ == "__main__":
    main()