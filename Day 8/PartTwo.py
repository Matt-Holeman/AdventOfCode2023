import math

MAX_LOOPS=200

def main():
    file = open("input.txt")
    mapDict = {}
    solve = 1
    for line in file:
        if "=" in line:
            line = line.replace('= (', '').replace(',', '').replace(')', '').strip()
            splitList = line.split(' ')
            mapDict[splitList[0]] = (splitList[1], splitList[2])
        elif "R" in line or "L" in line:
            sequence = line.strip()
    for s in findStarts(mapDict):
        solve = math.lcm(solve, walkPath(mapDict, sequence, s))
    print(solve)

def walkPath(mapDict, sequence, step):
    found = False
    count = 0
    for _ in range(MAX_LOOPS):
        for x in range(len(sequence)):
            c = sequence[x]
            if c == "L":
                stepKey = step[0]
            elif c == "R":
                stepKey = step[1]

            step = mapDict[stepKey]
            count += 1
            
            if stepKey.endswith('Z'):
                found = True
                break
        if found:
            break
    return count

def findStarts(mapDict):
    outList = []
    for key in mapDict.keys():
        if key.endswith("A"):
            outList.append(mapDict[key])
    return outList

if __name__ == "__main__":
    main()