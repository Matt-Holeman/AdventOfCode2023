MAX_LOOPS=200

def main():
    file = open("input.txt")
    mapDict = {}
    for line in file:
        if "=" in line:
            line = line.replace('= (', '').replace(',', '').replace(')', '').strip()
            splitList = line.split(' ')
            mapDict[splitList[0]] = (splitList[1], splitList[2])
        elif "R" in line or "L" in line:
            sequence = line.strip()
    print(walkPath(mapDict, sequence))

def walkPath(mapDict, sequence):
    step = mapDict['AAA']
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
            
            if stepKey == "ZZZ":
                found = True
                break
        if found:
            break
    return count

if __name__ == "__main__":
    main()