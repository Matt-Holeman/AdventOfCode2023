import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    file = open("input.txt")
    print(calculatePower(generateBoxDictionary(consumeFile(file))))

def generateBoxDictionary(hashList):
    boxDict = {}
    for opStr in hashList:
        if '-' in opStr:
            label = opStr.split('-')[0]
            hashLabel = hashString(label)
            if hashLabel in boxDict and label in boxDict[hashLabel]:
                boxDict[hashLabel].pop(label)
                if len(boxDict[hashLabel].keys()) < 1:
                       boxDict.pop(hashLabel)
        elif '=' in opStr:
            label, value = opStr.split('=')
            value = int(value)
            hashLabel = hashString(label)
            if hashLabel in boxDict:
                boxDict[hashLabel][label] = value
            else:
                boxDict[hashLabel] = {label : value}
    return boxDict

def calculatePower(boxDict):
    score = 0
    for boxKey in boxDict.keys():
        box = boxDict[boxKey]
        lenIdx = 1
        for lens in box.keys():
            score += (boxKey + 1) * lenIdx * box[lens]
            lenIdx += 1
    return score

def hashString(inString):
    value = 0
    for c in inString:
        value += ord(c)
        value *= 17
        value = value % 256
    return value

def consumeFile(file):
    return file.read().strip().split(',')

if __name__ == "__main__":
    main()