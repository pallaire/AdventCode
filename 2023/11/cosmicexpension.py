def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append(aline.strip())
        return res

def minimalDistancesSum(data, expandValue):
    h = len(data)
    w = len(data[1])

    # get empty rows and empty cols
    rowsCount = [0]*h
    colsCount = [0]*w

    # print(data)

    galaxies = []

    for y in range(h):
        for x in range(w):
            if data[y][x] == '.':
                rowsCount[y] += 1
                colsCount[x] += 1
            elif data[y][x] == '#':
                galaxies.append([y,x])

    galaxiesCount = len(galaxies)
    visited = set()

    sum = 0

    for loopa in range(galaxiesCount):
        for loopb in range(galaxiesCount):

            a = loopa
            b = loopb

            if a == b:
                continue

            if b < a:
                tmpa = a
                a = b
                b = tmpa

            label = f"{a}x{b}"

            if label in visited:
                continue

            visited.add(label)

            ax = galaxies[a][1]
            ay = galaxies[a][0]
            bx = galaxies[b][1]
            by = galaxies[b][0]

            sx = min(ax, bx)
            ex = max(ax, bx)
            sy = min(ay, by)
            ey = max(ay, by)

            dx = abs(bx - ax)
            dy = abs(by - ay)

            doublex = 0
            doubley = 0
            for x in range(dx):
                if colsCount[sx + x] == h:
                    doublex += expandValue - 1

            for y in range(dy):
                if rowsCount[sy + y] == w:
                    doubley += expandValue - 1

            sum += dx + dy + doublex + doubley

    return sum


data = readData("large.data")

print(f"Problem 1 - minimal distances sum = {minimalDistancesSum(data, 2)}")

print(f"Problem 2 - minimal distances sum = {minimalDistancesSum(data, 1000000)}")
