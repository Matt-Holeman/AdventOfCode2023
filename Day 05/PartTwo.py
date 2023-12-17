import json

def main():
    file = open("input.txt")
    fileList = consumeFile(file)
    mapDict = processFile(fileList)

    min = 0
    max = 60000000
    
    searchRange(min, max, mapDict)    


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
            mapDict['seeds'] = [ int(x) for x in line.removeprefix("seeds: ").strip().split(' ')]
        elif "-to-" in line:
            tmpList = []
            for x in range(i+1, len(fileList)):
                if fileList[x].replace(' ','').strip().isnumeric():
                    tmpList.append([ int(x) for x in fileList[x].strip().split(' ')])
                else:
                    break
            mapDict[line.replace(" map:", "").strip()] = tmpList
    return mapDict

def reverseMapValue(dictKey, sourceValue, mapDict):
    for mapRange in mapDict[dictKey]:
        if sourceValue >= int(mapRange[0]) and sourceValue < (int(mapRange[0]) + int(mapRange[2])):
            return sourceValue + (int(mapRange[1]) - int(mapRange[0]))
    return sourceValue

def searchRange(min, max, mapDict):
    percentageGate = 0.1
    found = False
    for x in range(int(min), int(max), 1):
        runningValue = x
        if ((x - min) / (max - min)) * 100 > percentageGate:
            print(f"=== {x} ({round((x - min) / (max - min) * 100)}%) ===")
            percentageGate += 0.1 
        for mapType in list(mapDict.keys())[::-1]:
            if mapType != 'seeds':
                runningValue = reverseMapValue(mapType, runningValue, mapDict)
        for i in range(len(mapDict['seeds'])):
            if i % 2 == 0:
                if runningValue >= mapDict['seeds'][i] and runningValue < (mapDict['seeds'][i] + mapDict['seeds'][i+1]):
                    print(f"FOUND! ({x})")
                    found = True
                    break
        if found:
            break

if __name__ == "__main__":
    main()