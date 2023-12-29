import copy

def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append(aline.strip())
        return res
    

def calculateNorthLoad(data):
    load = 0
    h = len(data)
    w = len(data[0])

    minHeights = [0] * w

    for y in range(h):
        for x in range(w):
            c = data[y][x]

            if c == '#':
                minHeights[x] = y+1
            elif c == 'O':
                load += h - minHeights[x]
                minHeights[x] += 1
    return load

def tilt(data, h, w, direction):
    if direction == 'n':
        minHeights = [0] * w
        for y in range(h):
            for x in range(w):
                c = data[y][x]
                if c == '#':
                    minHeights[x] = y+1
                elif c == 'O':
                    data[y][x] = '.'
                    data[minHeights[x]][x] = 'O'
                    minHeights[x] += 1

    elif direction == 'e':
        maxWidth = [w-1] * h
        for y in range(h):
            for x in range(w-1, -1, -1):
                c = data[y][x]
                if c == '#':
                    maxWidth[y] = x-1
                elif c == 'O':
                    data[y][x] = '.'
                    data[y][maxWidth[y]] = 'O'
                    maxWidth[y] -= 1

    elif direction == 's':
        maxHeights = [h-1] * w
        for y in range(h-1,-1,-1):
            for x in range(w):
                c = data[y][x]
                if c == '#':
                    maxHeights[x] = y-1
                elif c == 'O':
                    data[y][x] = '.'
                    data[maxHeights[x]][x] = 'O'
                    maxHeights[x] -= 1

    elif direction == 'w':
        minWidth = [0] * h
        for y in range(h):
            for x in range(w):
                c = data[y][x]
                if c == '#':
                    minWidth[y] = x+1
                elif c == 'O':
                    data[y][x] = '.'
                    data[y][minWidth[y]] = 'O'
                    minWidth[y] += 1

    return data


def print2D(data):
    for aline in data:
        print(''.join(aline))
    print()

def listhash(data):
    work = ''
    for aline in data:
        work += ''.join(aline)

    return hash(work)



def spin(data):
    global hashed
    h = len(data)
    w = len(data[0])

    splitted = []
    for y in range(h):
        splitted.append(list(data[y]))

    res = splitted
    tiltcache = {}
    hashed = 0

    currenthash = listhash(res)
    prevhash = None

    for i in range(1000000000):
        if currenthash in tiltcache:
            prevhash = currenthash
            currenthash = tiltcache[currenthash]["next"]
            continue
        else:
            tiltcache[currenthash] = {"data":copy.deepcopy(res), "next":None}

        res = tilt(res, h, w, 'n')
        res = tilt(res, h, w, 'w')
        res = tilt(res, h, w, 's')
        res = tilt(res, h, w, 'e')

        newhash = listhash(res)
        tiltcache[currenthash]["next"] = newhash
        currenthash = newhash
        
    res = tiltcache[currenthash]["data"]
    load = 0
    for y in range(h):
        for x in range(w):
            c = res[y][x]
            if c == 'O':
                load += h - y

    return load
    


data = readData("large.data")
print(f"Problem 1 - load : {calculateNorthLoad(data)}")
print(f"Problem 2 - spin load : {spin(data)}")