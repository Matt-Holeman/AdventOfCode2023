import json

def main():
    file = open("input-example.txt")
    fileList = consumeFile(file)
    mapDict = processFile(fileList)
    lowestValue = -1
    for seedValue in mapDict['seeds']:
        mapValue('seed-to-soil', int(seedValue), mapDict)
    for seedValue in mapDict['seeds']:
        runningValue = seedValue
        for key in mapDict.keys():
            if key != 'seeds':
                runningValue = mapValue(key, int(runningValue), mapDict)
                print(f"{key} --> {runningValue}")
            else:
                print(f"{key} --> {runningValue}")
        if runningValue < lowestValue or lowestValue == -1:
            lowestValue = runningValue
        print("===")
    print(lowestValue)

def consumeFile(file):
    outList = []
    for line in file:
        outList.append(line)
    return outList

def processFile(fileList):
    mapDict = {}
    for i in range(len(fileList)):
        line = fileList[i]
        if "seeds:" in line:
            mapDict['seeds'] = line.removeprefix("seeds: ").strip().split(' ')
        elif "-to-" in line:
            tmpList = []
            for x in range(i+1, len(fileList)):
                if fileList[x].replace(' ','').strip().isnumeric():
                    tmpList.append([ int(x) for x in fileList[x].strip().split(' ')])
                else:
                    break
            mapDict[line.replace(" map:", "").strip()] = tmpList
    return mapDict

def mapValue(dictKey, seedValue, mapDict):
    for mapRange in mapDict[dictKey]:
        if seedValue >= int(mapRange[1]):
            if seedValue <= mapRange[1] + mapRange[2]:
                # print(f"Seed: {seedValue}, Out: {seedValue + (mapRange[0] - mapRange[1])}, map: {mapRange}")
                return seedValue + (mapRange[0] - mapRange[1])
    # print(f"Seed: {seedValue}, Out: {seedValue}, map: none suitable")
    return seedValue

def test():
    print(79 <= 50 + 48)

if __name__ == "__main__":
    main()