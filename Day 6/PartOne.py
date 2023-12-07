
def main():
    file = open("input.txt")
    raceList = consumeFile(file)
    print(evaluateRaces(raceList))

def consumeFile(file):
    for line in file:
        if 'Time: ' in line:
            timeList = [ int(x) for x in ' '.join(line.removeprefix('Time:').split()).split(' ')]
            continue
        if 'Distance: ' in line:
            distanceList = [ int(x) for x in ' '.join(line.removeprefix('Distance:').split()).split(' ')]
            continue

    return [(timeList[x], distanceList[x]) for x in range(len(timeList))]

def evaluateRaces(raceList):
    product = 0
    for race in raceList:
        count = 0
        recordDistance = race[1]
        maxTime = race[0]
        for t in range(race[0]+1):
            if(t * (maxTime - t)) > recordDistance:
                count += 1
        product = max(product, 1) * count
    return product

        


if __name__ == "__main__":
    main()