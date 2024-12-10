from aoc import *

def walk(topo, w, h, x, y, target):
    if x<0 or x>=w or y<0 or y>=h:
        return []
    
    t = topo[y][x]
    if t != str(target):
        return []
    
    if t == '9':
        # done for this path
        return [(x,y)]
    
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]

    res = []
    for d in dirs:
        res.extend(walk(topo, w, h, x+d[0], y+d[1], target+1))
    return res

def findTrails(lines):
    h = len(lines)
    w = len(lines[1])

    heads = []

    # search for trail heads
    for y in range(h):
        for x in range(w):
            c = lines[y][x]
            if c == '0':
                heads.append((x,y))

    # for each head find paths:
    trails = []
    for hd in heads:
        trails.append(walk(lines, w, h, hd[0], hd[1], 0))
    return trails

def part1(lines):
    trails = findTrails(lines)
    res = 0
    for t in trails:
        res += len(set(t))
    return res


def part2(lines):
    trails = findTrails(lines)
    res = 0
    for t in trails:
        res += len(t)
    return res


AoCRunnerAll(10, 'Hoof It', part1, part2)
