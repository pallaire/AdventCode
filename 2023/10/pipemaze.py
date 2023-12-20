import math
import numpy as np

def readData(filename):
    with open(filename) as inputfile:
        return inputfile.readlines()
    

def cleanData(data):
    res = []

    for aline in data:
        res.append(aline.strip())
    return res

def printMaze(data):
    h = len(data)
    w = len(data[0])

    mazeFont = {'F':'┌', '7':'┐', 'J':'┘', 'L':'└', '-':'─', '|':'│'}

    for y in range(h):
        for x in range(w):
            c = data[y][x]
            c = mazeFont.get(c, c)
            print(c, end="")
        print()

def alloc2DCharArray(w, h, c):
    res = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append(c)
        res.append(row)
    return res

def scaleMazeByThree(data):
    h = len(data)
    w = len(data[0])
    sw = w * 3
    sh = h * 3

    scaledData = alloc2DCharArray(sw, sh, '?') 

    mazeScale = {'F':['???',
                      '?F-',
                      '?|?'], 
                 '7':['???',
                      '-7?',
                      '?|?'], 
                 'J':['?|?',
                      '-J?',
                      '???'], 
                 'L':['?|?',
                      '?L-',
                      '???'], 
                 '-':['???',
                      '---',
                      '???'], 
                 '|':['?|?',
                      '?|?',
                      '?|?'],
                 'S':['?S?',
                      'SSS',
                      '?S?'],
                 '.':['???',
                      '?.?',
                      '???'], }
    
    for y in range(h):
        for x in range(w):
            c = data[y][x]

            sx = x * 3
            sy = y * 3

            if c in mazeScale:
                s = mazeScale[c]

                for deltay in range(3):
                    for deltax in range(3):
                        scaledData[sy+deltay][sx + deltax] = s[deltay][deltax]
    return scaledData



def solveMazeMaxDistance(data, getContainedTiles):
    h = len(data)
    w = len(data[0])

    visited = set()
    toVisitStack = []

    # Find start
    for y in range(len(data)):
        x = data[y].find("S")
        if x != -1:
            toVisitStack.append({'x':x, 'y':y, 'count':0, "path":[]})
            break

    maxDistance = 0
    maxPath = []

    moves = [{"distance":[-1, 0], "types":"|F7"}, 
             {"distance":[ 1, 0], "types":"|LJ"}, 
             {"distance":[ 0,-1], "types":"-LF"}, 
             {"distance":[ 0, 1], "types":"-J7"}]


    while len(toVisitStack) > 0:
        abranch = toVisitStack.pop(0)
        y = abranch['y']
        x = abranch['x']
        count = abranch['count']
        currentPath = abranch['path']

        positionLabel = f"y:{abranch['y']},x:{abranch['x']},"

        if positionLabel in visited:
            continue
        else:
            visited.add(positionLabel)
            currentPath.append({"x":x, "y":y})

        for m in moves:
            dy = y + m["distance"][0]
            dx = x + m["distance"][1]

            if dy < 0 or dy >= h:
                continue

            if dx < 0 or dx >= w:
                continue

            dpipe = data[dy][dx]
            
            if dpipe == "S":
                # print(f"One loop done with count = {count}")
                if count > maxDistance:
                    maxDistance = count
                    maxPath = currentPath.copy()

                maxDistance = max(maxDistance, count)

            elif m["types"].find(dpipe) != -1:
                toVisitStack.insert(0, {'x':dx, 'y':dy, 'count':count+1, "path": currentPath.copy()})

    if getContainedTiles:
        # clean path
        cleaned = alloc2DCharArray(w, h, '.')
        for pos in maxPath:
            x = pos['x']
            y = pos['y']
            cleaned[y][x] = data[y][x]

        # Scale Maze
        scaled = scaleMazeByThree(cleaned)
        sh = len(scaled)
        sw = len(scaled[0])

        tovisit = [[0,0], [sh-1,0], [0, sw-1], [sh-1, sw-1]]
        visited = set()

        while len(tovisit) > 0:
            pos = tovisit.pop(0)
            x = pos[1]
            y = pos[0]

            if x < 0 or x >= sw or y < 0 or y >= sh:
                continue

            c = scaled[y][x]
            label = f"{y}-{x}"

            if label in visited:
                continue

            visited.add(label)

            if c == '?' or c == '.':
                scaled[y][x] = ' '
                tovisit.append([y-1, x])
                tovisit.append([y+1, x])
                tovisit.append([y, x-1])
                tovisit.append([y, x+1])

        count = 0

        for y in range(sh):
            for x in range(sw):
                c = scaled[y][x]

                if c == '.':
                    count += 1
                elif c == '?':
                    scaled[y][x] = ' '

        # printMaze(scaled)
        return count

    else:
        return math.ceil(maxDistance / 2)


data = cleanData(readData("/home/pallaire/devs/AdventCode/2023/10/large.data"))
print(f"Problem 1 : Max distance = {solveMazeMaxDistance(data, False)}")

print(f"Problem 2 : Contained tiles = {solveMazeMaxDistance(data, True)}")