from aoc import *

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

def floodSelect(field, w, h, x, y, c):
    res = set()

    if x<0 or x>=w or y<0 or y>=h:
        return res

    if field[y][x] != c:
        return res
    
    res.add((x,y))
    field[y][x] = '.'

    for d in dirs:
        res.update(floodSelect(field, w, h, x+d[0], y+d[1], c))
    return res

def findRegions(lines):
    h = len(lines)
    w = len(lines[0])

    # convert list of string to list of list of char
    # because string do not support element assignation
    field = [list(x) for x in lines]

    # find regions
    regions = []
    for y in range(h):
        for x in range(w):
            c = lines[y][x]
            if c != '.':
                flooded = floodSelect(field, w, h, x, y, c)
                if len(flooded) > 0:
                    regions.append(flooded)
    return regions

def perimeter(region):
    res = 0
    for pos in region:
        sides = 4
        for d in dirs:
            if (pos[0]+d[0], pos[1]+d[1]) in region:
                sides -= 1
        res += sides
    return res


def sides(region):
    res = 0
    minx = min(r[0] for r in region)
    miny = min(r[1] for r in region)
    maxx = max(r[0] for r in region)
    maxy = max(r[1] for r in region)

    # from left to right
    for x in range(minx, maxx+1):
        prevfound = -1
        for y in range(miny, maxy+1):
            pos = (x,y)
            if pos in region and (pos[0]-1, pos[1]) not in region:
                if prevfound == -1:
                    res += 1
                prevfound = y
            else:
                prevfound = -1

    # from left to right
    for x in range(maxx, minx-1, -1):
        prevfound = -1
        for y in range(miny, maxy+1):
            pos = (x,y)
            if pos in region and (pos[0]+1, pos[1]) not in region:
                if prevfound == -1:
                    res += 1
                prevfound = y
            else:
                prevfound = -1

    # from top to bottom
    for y in range(miny, maxy+1):
        prevfound = -1
        for x in range(minx, maxx+1):
            pos = (x,y)
            if pos in region and (pos[0], pos[1]-1) not in region:
                if prevfound == -1:
                    res += 1
                prevfound = x
            else:
                prevfound = -1

    # from bottom to top
    for y in range(maxy, miny-1, -1):
        prevfound = -1
        for x in range(minx, maxx+1):
            pos = (x,y)
            if pos in region and (pos[0], pos[1]+1) not in region:
                if prevfound == -1:
                    res += 1
                prevfound = x
            else:
                prevfound = -1
    return res

def part1(lines):
    regions = findRegions(lines)
    res = 0
    for r in regions:
        res += len(r) * perimeter(r)
    return res

def part2(lines):
    regions = findRegions(lines)
    res = 0
    for r in regions:
        res += len(r) * sides(r)
    return res

AoCRunnerAll(12, 'Garden Groups', part1, part2)
