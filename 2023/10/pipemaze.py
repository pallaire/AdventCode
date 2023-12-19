import math

def readData(filename):
    with open(filename) as inputfile:
        return inputfile.readlines()
    

def cleanData(data):
    res = []

    for aline in data:
        res.append(aline.strip())
    return res



def solveMazeMaxDistance(data):
    h = len(data)
    w = len(data[0])
    sx = -1
    sy = -1

    visited = set()
    toVisitStack = []

    # Find start
    for y in range(len(data)):
        x = data[y].find("S")
        if x != -1:
            toVisitStack.append({'x':x, 'y':y, 'count':0})
            sx = x
            sy = y
            break

    maxDistance = 0

    moves = [{"distance":[-1, 0], "types":"|F7"}, 
             {"distance":[ 1, 0], "types":"|LJ"}, 
             {"distance":[ 0,-1], "types":"-LF"}, 
             {"distance":[ 0, 1], "types":"-J7"}]


    while len(toVisitStack) > 0:
        abranch = toVisitStack.pop(0)
        y = abranch['y']
        x = abranch['x']
        count = abranch['count']

        positionLabel = f"y:{abranch['y']},x:{abranch['x']},"
        print(f"{positionLabel} with count {count}")

        if positionLabel in visited:
            print(f"Warning, would loop at {positionLabel}")
            continue
        else:
            visited.add(positionLabel)

        for m in moves:
            dy = y + m["distance"][0]
            dx = x + m["distance"][1]

            if dy < 0 or dy >= h:
                continue

            if dx < 0 or dx >= w:
                continue

            dpipe = data[dy][dx]
            
            if dpipe == "S":
                print(f"One loop done with count = {count}")
                maxDistance = max(maxDistance, count)

            elif m["types"].find(dpipe) != -1:
                toVisitStack.insert(0, {'x':dx, 'y':dy, 'count':count+1})



    return math.ceil(maxDistance / 2)


data = cleanData(readData("large.data"))
print(f"Problem 1 : Max distance = {solveMazeMaxDistance(data)}")