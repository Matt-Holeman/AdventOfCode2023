def main():
    filename = "./input.txt"
    file = open(filename)
    x = firstLineSize(filename) + 1
    y = countLines(filename)
    matrix = consumeFile(file, x, y)
    symbols = findSymbols(matrix)
    hitDict = evaluateNums(matrix, symbols)

    count = 0
    for hit in hitDict.keys():
        mult = 1
        if len(hitDict[hit]) > 1:
            for num in hitDict[hit]:
                mult *= int(num)
            count += mult
    print(count)

def consumeFile(file, x, y):
    matrix = [[ 0 for i in range(x) ] for j in range(y) ]
    x = 0
    for line in file:
        line = line.strip()
        line = line + " "
        y = 0
        for c in line:
            matrix[x][y] = c
            y += 1
        x += 1
    return matrix

def findSymbols(matrix):
    symbols = []
    x = 0
    for row in matrix:
        y = 0
        for cell in row:
            if cell == '*':
                symbols += [[x,y]]
            y += 1
        x += 1
    return symbols

def evaluateNums(matrix, symbols):
    x = 0
    numString = ""
    hit = False
    hitDict = {}
    symbolCoord = ""
    for row in matrix:
        y = 0
        for cell in row:
            coord = [x,y]
            if cell in "1234567890":
                numString += cell
                tmpSymbolCoord = evaluateSymbolProximity(coord, symbols)
                if tmpSymbolCoord != -1:
                    symbolCoord = tmpSymbolCoord
                    hit = True
            else:
                if hit:
                    if symbolCoord in hitDict:
                        tmpList = hitDict[symbolCoord]
                        tmpList.append(numString)
                        hitDict[symbolCoord] = tmpList
                    else:
                        hitDict[symbolCoord] = [numString]
                    print(hitDict)
                numString = ""
                hit = False
                symbolCoord = ""
            y += 1
        x += 1
    return hitDict

def evaluateSymbolProximity(coordinate, symbols):
    for symbol in symbols:
        if abs(symbol[0] - coordinate[0]) <= 1 and abs(symbol[1] - coordinate[1]) <= 1:
            print(f"{symbol[0]}{symbol[1]}")
            return f"{symbol[0]}{symbol[1]}"
    return -1


def firstLineSize(filename):
    file = open(filename)
    length = len(file.readline().strip())
    file.close()
    return length

def countLines(filename):
    file = open(filename)
    count = sum(1 for _ in file)
    file.close()
    return count
            


if __name__ == "__main__":
    main()