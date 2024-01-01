import re

def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append([int(x) for x in re.findall(r"\d", aline)])
        return res


kUp = 0
kRight = 1
kDown = 2
kLeft = 3

kMoves = {kUp:{'x':0, 'y':-1},
          kRight:{'x':1, 'y':0},
          kDown:{'x':0, 'y':1},
          kLeft:{'x':-1, 'y':0} }

# This is a path finding problem
# Dijkstra algo
def findLeastHeatPath(data):
    h = len(data)
    w = len(data[0])

    endX = w-1
    endY = h-1

    stateQueueByCost = {}
    seenCostByState = {}

    def addState(x, y, cost, direction, distance):
        if x<0 or y<0 or x>=w or y>=h:
            return -1

        newCost = cost + data[y][x]


        if x==endX and y==endY:
            return newCost

        state = (x,y, direction, distance)

        if state not in seenCostByState:
            # add the state to the queue to visit later
            if newCost in stateQueueByCost:
                stateQueueByCost[newCost].append(state)
            else:
                stateQueueByCost[newCost] = [state]

            # mark this state as seen
            seenCostByState[state] = newCost
        return 0

    # add the initial state
    # skip the 0,0, start on tiles next to it, so that we wont count it's heat
    addState(1, 0, 0, kRight, 1)
    addState(0, 1, 0, kDown, 1)

    while True:
        # get the lowest cost/heat in the queue of state to visit
        currentcost = min(stateQueueByCost.keys())

        # get all states with the same cost
        states = stateQueueByCost.pop(currentcost)

        # check for new state all around the states at that cost
        for astate in states:
            (x, y, direction, distance) = astate

            leftdir = (direction + 4 - 1) % 4
            rightdir = (direction + 1) % 4

            # turn  left
            res = addState(x+kMoves[leftdir]['x'], y+kMoves[leftdir]['y'], currentcost, leftdir, 1)
            if res>0:
                return res

            # turn right
            res = addState(x+kMoves[rightdir]['x'], y+kMoves[rightdir]['y'], currentcost, rightdir, 1)
            if res>0:
                return res

            # continue straight
            if distance < 3:
                res = addState(x+kMoves[direction]['x'], y+kMoves[direction]['y'], currentcost, direction, distance+1)
                if res>0:
                    return res


data = readData("/home/pallaire/devs/AdventCode/2023/17/large.data")
print(f"Problem 1: Heat={findLeastHeatPath(data)}")



