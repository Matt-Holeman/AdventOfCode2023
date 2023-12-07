def consumeFile(filename):
    file = open(filename)
    count = 0
    total = 0
    cardDict = {}
    for line in file:
        splitString = line[line.index(':')+2:].replace('  ', ' ').split('|')
        cardDict[count] = {'winning-nums' : splitString[0].strip().split(' '), 'held-nums' : splitString[1].strip().split(' '), 'duplicate-count': 1}
        count += 1
    for i in cardDict.keys():
        matches = 0
        card = cardDict[i]
        for n in card['held-nums']:
            if n in card['winning-nums']:
                matches += 1
        for x in range(i+1, i+1+matches, 1):
            cardDict[x]['duplicate-count'] += card['duplicate-count']
    for c in cardDict.keys():
        total += cardDict[c]['duplicate-count']
    return total

print(consumeFile("input.txt"))