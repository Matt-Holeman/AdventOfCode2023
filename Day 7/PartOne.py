RANKS="23456789TJQKA"
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
    handDict = {'hand' : a[0], 'bet' : a[1]}
    for rank in RANKS:
        diff = len(a[0]) - len(a[0].replace(rank, ''))
        if diff > 1:
            if diff in handDict:
                handDict[diff] += 1
            else:
                handDict[diff] = 1
    handDict['score'] = scoreHand(handDict)
    return handDict

def compareHands(a, b):
    """
    Return true if A is better than B
    """
    if a['score'] == b['score']:
        return compareHandRanks(a['hand'], b['hand'])
    else:
        return a['score'] > b['score']

def scoreHand(a):
    """
    High Card = 0
    One Pair = 1
    Two Pair = 2
    Three of a Kind = 3
    Full House = 4
    Four of a Kind = 5
    Five of a Kind = 6
    """
    score = 0
    for i in SCORES.keys():
       if i in a:
           score += (a[i] * SCORES[i])
    return score

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

if __name__ == "__main__":
    main()