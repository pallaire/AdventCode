import functools

def readData(filename):
    with open(filename) as inputfile:
        return inputfile.readlines()
    
kFive       = 7
kFour       = 6
kFullHouse  = 5
kThree      = 4
kTwoPair    = 3
kOnePair    = 2
kHighCard   = 1

def getHandType(hand, useJocker):
    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1

    jockerCount = 0
    if useJocker:
        jockerCount = cards.get("J", 0)

    maxCount = max(cards.values())
    minCount = min(cards.values())
    if maxCount == 5:
        return kFive
    elif maxCount == 4:
        if jockerCount == 1 or jockerCount == 4:
            return kFive
        return kFour
    elif maxCount == 3:
        if minCount == 2:
            if jockerCount == 3 or jockerCount == 2:
                return kFive
            return kFullHouse
        else:
            if jockerCount == 3 or jockerCount == 1:
                return kFour
            return kThree
    elif maxCount == 2:
        if len(cards.keys()) == 3:
            if jockerCount == 1:
                return kFullHouse
            elif jockerCount == 2:
                return kFour
            return kTwoPair
        else:
            if jockerCount == 2 or jockerCount == 1:
                return kThree
            return kOnePair

    if jockerCount == 1:
        return kOnePair

    return kHighCard        
    
def compareHands(a, b):
    if b[0] != a[0]:
        return b[0] - a[0]
    
    cardvalues = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    for i in range(5):
        ca = cardvalues[a[1][i]]
        cb = cardvalues[b[1][i]]
        if cb != ca:
            return cb - ca
    return 0

def compareHandsLowJ(a, b):
    if b[0] != a[0]:
        return b[0] - a[0]
    
    cardvalues = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':1, 'Q':12, 'K':13, 'A':14}
    for i in range(5):
        ca = cardvalues[a[1][i]]
        cb = cardvalues[b[1][i]]
        if cb != ca:
            return cb - ca
    return 0


def parseCards(data, useJocker):
    hands = []
   
    for aline in data:
        tokens = aline.split(" ")
        hand = tokens[0]
        bet = int(tokens[1])
        handtype = getHandType(hand, useJocker)
        hands.append([handtype, hand, bet])
    
    if useJocker:
        hands = sorted(hands, key=functools.cmp_to_key(compareHandsLowJ))
    else:
        hands = sorted(hands, key=functools.cmp_to_key(compareHands))
  
    total = 0
    handscount = len(hands)
    for i in range(handscount):
        total += (handscount-i) * hands[i][2]

    return total


data = readData("large.data")
print(f"Problem 1 - hands value = {parseCards(data, False)}")
print(f"Problem 2 - hands value = {parseCards(data, True)}")