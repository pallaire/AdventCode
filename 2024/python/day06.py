from aoc import *

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

def part1(lines):
    (floormap, startpos, w, h, visited) = floorScanAndPath(lines)
    return len(visited)

def part2(lines):
    (floormap, startpos, w, h, visited) = floorScanAndPath(lines)

    loops = 0
    for obs in visited.keys():
        if obs == startpos:
            continue

        # add temp obstruction
        floormap.add(obs)

        # Walk the new maze
        guardpos = startpos
        guarddir = 0
        obsvisited = {}
        itsaloop = False
        while(guardpos[0]>=0 and guardpos[0]<w and guardpos[1]>=0 and guardpos[1]<h):
            if guardpos in obsvisited:
                if guarddir in obsvisited[guardpos]:
                    itsaloop = True
                    break
                else:
                    obsvisited[guardpos].append(guarddir)
            else:
                obsvisited[guardpos] = [guarddir]
            destination = (guardpos[0] + dirs[guarddir][0], guardpos[1] + dirs[guarddir][1])
            if destination in floormap:
                guarddir = (guarddir+1)%4
            else:
                guardpos = destination

        if itsaloop:
            loops += 1

        # remove temp obstruction
        floormap.remove(obs)

    return loops

AoCRunnerAll(6, 'Guard Gallivant', part1, part2)