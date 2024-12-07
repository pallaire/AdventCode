from aoc import *
from itertools import repeat
from multiprocessing import Pool

# up, right, down, left
dirs = [(0,-1), (1,0), (0,1), (-1,0)]

def floorScanAndPath(lines):
    floormap = set()
    h = len(lines)
    w = len(lines[0])
    startpos = (0,0)
    for y in range(h):
        for x in range(w):
            c = lines[y][x]
            if c == '#':
                floormap.add((x,y))
            elif c == '^':
                startpos = (x,y)

    visited = {}
    guardpos = startpos
    guarddir = 0
    while(guardpos[0]>=0 and guardpos[0]<w and guardpos[1]>=0 and guardpos[1]<h):
        visited[guardpos] = guarddir
        destination = (guardpos[0] + dirs[guarddir][0], guardpos[1] + dirs[guarddir][1])
        if destination in floormap:
            guarddir = (guarddir+1)%4
        else:
            guardpos = destination

    return (floormap, startpos, w, h, visited)

def checkForLoop(obstruction, floormap, w, h, startpos):
    if startpos == obstruction:
        return 0
    
    guardpos = startpos
    guarddir = 0
    visited = {}
    itsaloop = False
    while(guardpos[0]>=0 and guardpos[0]<w and guardpos[1]>=0 and guardpos[1]<h):
        if guardpos in visited:
            if guarddir in visited[guardpos]:
                return 1
            else:
                visited[guardpos].append(guarddir)
        else:
            visited[guardpos] = [guarddir]
        destination = (guardpos[0] + dirs[guarddir][0], guardpos[1] + dirs[guarddir][1])
        if destination in floormap or destination==obstruction:
            guarddir = (guarddir+1)%4
        else:
            guardpos = destination
    return 0


def part1(lines):
    (floormap, startpos, w, h, visited) = floorScanAndPath(lines)
    return len(visited)

def part2(lines):
    (floormap, startpos, w, h, visited) = floorScanAndPath(lines)

    loops = 0
    with Pool() as pool:
        loops = sum(pool.starmap(checkForLoop, zip(visited.keys(), repeat(floormap), repeat(w), repeat(h), repeat(startpos))))

    return loops

AoCRunnerAll(6, 'Guard Gallivant', part1, part2)
