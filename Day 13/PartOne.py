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
        score += findRefectionRow(island)
        score += findReflectionColumn(island)
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

def findRefectionRow(island):
    score = 0
    for rowIdx in range(len(island)-1):
        if island[rowIdx] == island[rowIdx+1]:
            correct = True
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
                break
    return score 

def findReflectionColumn(island):
    island = island[::-1]
    score = 0
    for columnIdx in range(len(island[0])-1):
        if "".join([x[columnIdx] for x in island]) == "".join([x[columnIdx+1] for x in island]):
            correct = True
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
                break
    return score

if __name__ == "__main__":
    main()