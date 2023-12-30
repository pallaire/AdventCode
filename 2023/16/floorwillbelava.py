def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append(aline.strip())
        return res


kTop = 1
kRight = 2
kBottom = 3
kLeft = 4
kMoves = {
    kTop:{'x':0, 'y':-1},
    kRight:{'x':1, 'y':0},
    kBottom:{'x':0, 'y':1},
    kLeft:{'x':-1, 'y':0}
    }

def printData(data):
    for aline in data:
        print(aline)

def energize(data, start):
    h = len(data)
    w = len(data[0])

    energized = [[0]*w for _ in range(h)]
    stack = [start]
    done = set()

    while len(stack) > 0:
        move = stack.pop()
        x = move['x']
        y = move['y']
        dir = move['dir']

        if x<0 or y<0 or x>=w or y>=h:
            # out of bound
            continue

        energized[y][x] += 1
        c = data[y][x]

        label = f"{x}x{y}->{dir}   char={c}"
        # print(label)

        if not label in done:
            done.add(label)

            if c == '.':
                # we continue
                stack.append({'x':x+kMoves[dir]['x'], 'y':y+kMoves[dir]['y'], 'dir':dir})
            elif c == '|':
                if dir == kTop or dir == kBottom:
                    # we continue
                    stack.append({'x':x+kMoves[dir]['x'], 'y':y+kMoves[dir]['y'], 'dir':dir})
                else:
                    stack.append({'x':x+kMoves[kTop]['x'], 'y':y+kMoves[kTop]['y'], 'dir':kTop})
                    stack.append({'x':x+kMoves[kBottom]['x'], 'y':y+kMoves[kBottom]['y'], 'dir':kBottom})
            elif c == '-':
                if dir == kLeft or dir == kRight:
                    # we continue
                    stack.append({'x':x+kMoves[dir]['x'], 'y':y+kMoves[dir]['y'], 'dir':dir})
                else:
                    stack.append({'x':x+kMoves[kLeft]['x'], 'y':y+kMoves[kLeft]['y'], 'dir':kLeft})
                    stack.append({'x':x+kMoves[kRight]['x'], 'y':y+kMoves[kRight]['y'], 'dir':kRight})
            elif c == '/':
                if dir == kTop:
                    stack.append({'x':x+kMoves[kRight]['x'], 'y':y+kMoves[kRight]['y'], 'dir':kRight})
                elif dir == kBottom:
                    stack.append({'x':x+kMoves[kLeft]['x'], 'y':y+kMoves[kLeft]['y'], 'dir':kLeft})
                elif dir == kLeft:
                    stack.append({'x':x+kMoves[kBottom]['x'], 'y':y+kMoves[kBottom]['y'], 'dir':kBottom})
                elif dir == kRight:
                    stack.append({'x':x+kMoves[kTop]['x'], 'y':y+kMoves[kTop]['y'], 'dir':kTop})
            elif c == '\\':
                if dir == kBottom:
                    stack.append({'x':x+kMoves[kRight]['x'], 'y':y+kMoves[kRight]['y'], 'dir':kRight})
                elif dir == kTop:
                    stack.append({'x':x+kMoves[kLeft]['x'], 'y':y+kMoves[kLeft]['y'], 'dir':kLeft})
                elif dir == kRight:
                    stack.append({'x':x+kMoves[kBottom]['x'], 'y':y+kMoves[kBottom]['y'], 'dir':kBottom})
                elif dir == kLeft:
                    stack.append({'x':x+kMoves[kTop]['x'], 'y':y+kMoves[kTop]['y'], 'dir':kTop})
            else:
                print(f"wrong char -->  {c}")

    count = 0
    for y in range(h):
        for x in range(w):
            if energized[y][x] != 0:
                count += 1

    return count

def energizePerimeter(data):
    h = len(data)
    w = len(data[0])

    res = 0

    res = max(res, energize(data, {'x':0, 'y':0, 'dir':kBottom}))
    res = max(res, energize(data, {'x':0, 'y':0, 'dir':kRight}))
    res = max(res, energize(data, {'x':0, 'y':h-1, 'dir':kTop}))
    res = max(res, energize(data, {'x':0, 'y':h-1, 'dir':kRight}))
    res = max(res, energize(data, {'x':w-1, 'y':0, 'dir':kBottom}))
    res = max(res, energize(data, {'x':w-1, 'y':0, 'dir':kLeft}))
    res = max(res, energize(data, {'x':w-1, 'y':h-1, 'dir':kTop}))
    res = max(res, energize(data, {'x':w-1, 'y':h-1, 'dir':kLeft}))

    for y in range(h-2):
        res = max(res, energize(data, {'x':0, 'y':y, 'dir':kRight}))
        res = max(res, energize(data, {'x':w-1, 'y':y, 'dir':kLeft}))

    for x in range(w-2):
        res = max(res, energize(data, {'x':x, 'y':0, 'dir':kBottom}))
        res = max(res, energize(data, {'x':x, 'y':h-1, 'dir':kTop}))

    return res


data = readData("large.data")

res1 = energize(data, {'x':0, 'y':0, 'dir':kRight})
print(f"Problem 1 : {res1}")

res2 = energizePerimeter(data)
print(f"Problem 2 : {res2}")


