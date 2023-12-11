RANKS="J23456789TQKA"
SCORES={
    2 : 1,
    3 : 3,
    4 : 5,
    5 : 6
}

def main():
    file = open("input.txt")
    handList = bubbleSortHand(consumeFile(file))
    score = 0
    for i in range(len(handList)):
        score += (i+1) * handList[i]['bet']
    print(score)

def bubbleSortHand(handList):
    """
    Returns ordered list of hand objects
    """
    n = len(handList)
    swap = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if compareHands(handList[j],handList[j + 1]):
                swap = True
                handList[j], handList[j + 1] = handList[j + 1], handList[j]
        if not swap:
            return handList
    return handList

def consumeFile(file):
    """
    Format file into a list of tuples, first value the Hand information, second is the bet value
    """
    handList = []
    for line in file:
        split = line.split(' ')
        handList.append(consumeHand((split[0].strip(), int(split[1].strip()))))
    return handList

def consumeHand(a):
    """
    Formats a hand into a dictionary of grouped counts
    """
    a = convertJokers(a)
    handDict = {'hand' : a[0], 'true-hand': a[1], 'bet' : a[2]}
    handDict['score'] = scoreHand(a)
    return handDict

def compareHands(a, b):
    """
    Return true if A is better than B
    """
    if a['score'] == b['score']:
        return compareHandRanks(a['true-hand'], b['true-hand'])
    else:
        return a['score'] > b['score']

def compareHandRanks(a, b):
    """
    Returns true if Hand A > Hand B, purely based on Rank alone
    Equal hands raise error
    """
    for i in range(max(len(a),len(b))):
        if a[i] == b[i]:
            continue
        for rank in RANKS:
            if rank == a[i]:
                return False
            elif rank == b[i]:
                return True
    raise ValueError(f"Hands are equal ({a} === {b})")

def scoreHand(a):
    """
    x2 = 1
    x3 = 3
    x4 = 5
    x5 = 6
    ---
    High Card = 0
    One Pair = 1
    Two Pair = 2
    Three of a Kind = 3
    Full House = 4
    Four of a Kind = 5
    Five of a Kind = 6
    """
    handDict = {}
    score = 0
    for rank in RANKS:
        diff = len(a[0]) - len(a[0].replace(rank, ''))
        if diff > 1:
            if diff in handDict:
                handDict[diff] += 1
            else:
                handDict[diff] = 1
    for i in SCORES.keys():
       if i in handDict:
           score += (handDict[i] * SCORES[i])
    return score

def convertJokers(a):
    """
    Convert Jokers to the best possible cards, assume they convert to the same card
    """
    bestRank = -1
    bestScore = -1
    for rank in RANKS:
        b = (a[0].replace('J', rank), a[1])
        score = scoreHand(b)
        if score > bestScore or bestRank == -1:
            bestScore = score
            bestRank = rank
    return (a[0].replace('J',bestRank), a[0], a[1])

if __name__ == "__main__":
    main()