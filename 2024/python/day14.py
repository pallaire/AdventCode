from aoc import *
import re
from functools import reduce
from PIL import Image

def part1(lines):
    if len(lines) == 12:
        w = 11
        h = 7
    else:
        w = 101
        h = 103

    mw = w>>1
    mh = h>>1

    Qs = [0,0,0,0]

    for aline in lines:
        (x, y, dx, dy) = [int(x) for x in re.findall("-?\\d+", aline)]
        destx = (x + (dx*100))%w
        desty = (y + (dy*100))%h

        if destx==mw or desty==mh:
            continue

        q = 0
        if destx > mw:
            q = 1
        if desty > mh:
            q += 2

        Qs[q] += 1

    return reduce(lambda a,b: a*b, Qs)

def istree(tree, w, h):
    mw = w >> 1

    if tree[0][mw] != 1:
        return False

    for y in range(1, 5):
        if tree[y][mw-y] != 1:
            return False
        if tree[y][mw+y] != 1:
            return False
    
    return True

def printTreeAtSec(robots, w, h, sec):
    tree = []
    for y in range(h):
        tree.append([' ']*w)

    for (x, y, dx, dy) in robots:
        tx = (x + dx*sec)%w
        ty = (y + dy*sec)%h
        tree[ty][tx] = '*'

    for y in range(h):
        [print(t, end='') for t in tree[y]]
        print()

# We are searching visually for a small tree, 
# Not a large one that take the whole page
def part2(lines):
    if len(lines) == 12:
        w = 11
        h = 7
        # 11 * 7 == 77
    else:
        w = 101
        h = 103
        # 101 * 103 = 10403

    mw = w >> 1
    maxsecs = w * h

    robots = []
    for aline in lines:
        robots.append([int(x) for x in re.findall("-?\\d+", aline)])


    for sec in range(maxsecs):
        img = Image.new("1", (w, h))

        for (x, y, dx, dy) in robots:
            px = (x + dx*sec)%w
            py = (y + dy*sec)%h
            img.putpixel((px, py), 1)

        img.save(f"output/tree{sec:05}.png")

    return -1

AoCRunnerAll(14, 'Restroom Redoubt', part1, part2)
