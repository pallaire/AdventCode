import re

def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append(aline.strip())
        return res

kMoves = {'U':(0,-1), 'R':(1,0), 'D':(0,1), 'L':(-1,0)}

def printGround(ground):
    h = len(ground)
    w = len(ground[0])
    count = 0

    for y in range(h):
        for x in range(w):
            c = ground[y][x]
            if c[0] == '#':
                count += 1
                print('#', end='')
            else:
                print(c, end='')
        print()
    return count

def floodFill(ground, x, y):
    h = len(ground)
    w = len(ground[0])

    queue = [(x,y)]
    done = set()

    while len(queue) > 0:
        pos = queue.pop()
        (x,y) = pos

        if pos in done:
            continue

        if x<0 or y<0 or x>=w or y>=h:
            continue

        done.add(pos)

        if ground[y][x][0] == '#':
            continue

        if ground[y][x] == '.':
            ground[y][x] = ' '

        for m in ['U', 'R', 'D', 'L']:
            nx = x + kMoves[m][0]
            ny = y + kMoves[m][1]
            queue.append((nx,ny))

def extendGround(ground, x, y):
    h = len(ground)
    w = len(ground[0])

    if x < 0:
        for extendy in range(h):
            for _ in range(-x):
                ground[extendy].insert(0,'.')
    elif x > 0:
        for extendy in range(h):
            for _ in range(x):
                ground[extendy].append('.')
    elif y < 0:
        for _ in range(-y):
            ground.insert(0,['.']*w)
    elif y > 0:
        for _ in range(y):
            ground.append(['.']*w)
    return ground

def digRegionOnMap(data):
    w = 1
    h = 1
    x = 0
    y = 0

    ground = [['.']]

    for aline in data:

        # print()
        # print()
        # print()
        # print()
        # print(aline)

        matchres = re.match(r"(\w) (\d*) \((.*)\)", aline)
        (direction, distance, color) = matchres.groups()
        distance = int(distance)

        (dirx, diry) = kMoves[direction]
        distancex = dirx * distance
        distancey = diry * distance

        destx = x + distancex
        desty = y + distancey


        # extend the array if needed
        if destx < 0:
            addx = abs(destx)
            for extendy in range(h):
                for _ in range(addx):
                    ground[extendy].insert(0,'.')
            x += addx
            w += addx
        elif destx >= w:
            addx = destx - w + 1
            for extendy in range(h):
                for _ in range(addx):
                    ground[extendy].append('.')
            w += addx
        elif desty < 0:
            addy = abs(desty)
            for _ in range(addy):
                ground.insert(0,['.']*w)
            y += addy
            h += addy
        elif desty >= h:
            addy = desty - h + 1
            for _ in range(addy):
                ground.append(['.']*w)
            h += addy

        # move
        if distancex != 0:
            if distancex < 0:
                ex = x-1
                sx = ex+distancex+1
                x = sx
            else:
                sx = x+1
                ex = sx+distancex-1
                x = ex

            while sx <= ex:
                ground[y][sx] = color
                sx += 1
        else:
            if distancey < 0:
                ey = y-1
                sy = ey+distancey+1
                y = sy
            else:
                sy = y+1
                ey = sy+distancey-1
                y = ey

            while sy <= ey:
                ground[sy][x] = color
                sy += 1

    # Extend for better floodfill
    ground = extendGround(ground,1,0)
    ground = extendGround(ground,-1,0)
    ground = extendGround(ground,0,1)
    ground = extendGround(ground,0,-1)
    w += 2
    h += 2

    floodFill(ground, 0, 0)
    printGround(ground)

    count = 0
    for y in range(h):
        for x in range(w):
            if ground[y][x] != ' ':
                count += 1

    return count

def digRegion(data):
    points = []

    x = 0
    y = 0

    points.append((x,y))
    perimeter = 0

    for aline in data:
        matchres = re.match(r"(\w) (\d*) \((.*)\)", aline)
        (direction, distance, color) = matchres.groups()
        distance = int(distance)

        (dirx, diry) = kMoves[direction]
        x += dirx * distance
        y += diry * distance
        points.append((x,y))

        perimeter += distance

    # Polygon Area - Showlace Algo
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # for (int i = 0; i < numVertices - 1; ++i)
    #   area += point[i].x * point[i+1].y - point[i+1].x * point[i].y;
    # area += point[numVertices-1].x * point[0].y - point[0].x * point[numVertices-1].y;
    area = 0
    lenPoints = len(points)
    for i in range(lenPoints-1):
        area += points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1]
    # last instruction is not needed because our last point is equal to our first point
    # area += points[lenPoints-1][0]*points[0][1] - points[0][0]*points[lenPoints-1][1]

    # Now add half the perimeters for Pike's Theorem
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + p/2 - 1
    area = (abs(area) / 2) + (perimeter/2) + 1

    return int(area)


def digRegionSwapColorInstructions(data):

    x = 0
    y = 0

    points = []
    points.append((x,y))
    perimeter = 0

    # 0 means R, 1 means D, 2 means L, and 3 means U.
    kMovesSwapInstructions = {'3':(0,-1), '0':(1,0), '1':(0,1), '2':(-1,0)}

    for aline in data:
        # matchres = re.match(r"(\w) (\d*) \((.*)\)", aline)
        # (direction, distance, color) = matchres.groups()
        direction = aline[-2]
        distance = int(aline[-7:-2], 16)

        (dirx, diry) = kMovesSwapInstructions[direction]
        x += dirx * distance
        y += diry * distance
        points.append((x,y))

        perimeter += distance

    # Polygon Area - Showlace Algo
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # for (int i = 0; i < numVertices - 1; ++i)
    #   area += point[i].x * point[i+1].y - point[i+1].x * point[i].y;
    # area += point[numVertices-1].x * point[0].y - point[0].x * point[numVertices-1].y;
    area = 0
    lenPoints = len(points)
    for i in range(lenPoints-1):
        area += points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1]
    # last instruction is not needed because our last point is equal to our first point
    # area += points[lenPoints-1][0]*points[0][1] - points[0][0]*points[lenPoints-1][1]

    # Now add half the perimeters for Pike's Theorem
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + p/2 - 1
    area = (abs(area) / 2) + (perimeter/2) + 1
    
    return int(area)


data = readData("large.data")
print(f"Problem 1: {digRegion(data)}")
print(f"Problem 2 : {digRegionSwapColorInstructions(data)}")
