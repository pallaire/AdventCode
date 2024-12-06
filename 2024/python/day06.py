from aoc import *

def floorScan(lines):
    floormap = set()
    h = len(lines)
    w = len(lines[0])
    guardpos = (0,0)
    for y in range(h):
        for x in range(w):
            c = lines[y][x]
            if c == '#':
                floormap.add((x,y))
            elif c == '^':
                guardpos = (x,y)
    return (floormap, guardpos, w, h)

def part1(lines):
    (floormap, guardpos, w, h) = floorScan(lines)

    # up, right, down, left
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    guarddir = 0
    
    visited = {}
    while(guardpos[0]>=0 and guardpos[0]<w and guardpos[1]>=0 and guardpos[1]<h):
        visited[guardpos] = guarddir
        destination = (guardpos[0] + dirs[guarddir][0], guardpos[1] + dirs[guarddir][1])
        if destination in floormap:
            guarddir = (guarddir+1)%4
        else:
            guardpos = destination

    return len(visited)

def part2(lines):
    (floormap, guardpos, w, h) = floorScan(lines)

    # up, right, down, left
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    guarddir = 0
    
    startpos = guardpos
    visited = {}
    while(guardpos[0]>=0 and guardpos[0]<w and guardpos[1]>=0 and guardpos[1]<h):
        if guardpos in visited:
            visited[guardpos].append(guarddir)
        else:
            visited[guardpos] = [guarddir]
        destination = (guardpos[0] + dirs[guarddir][0], guardpos[1] + dirs[guarddir][1])
        if destination in floormap:
            guarddir = (guarddir+1)%4
        else:
            guardpos = destination

    validPosDir = {}
    invalidPosDir = {}
    res = 0

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
            if guardpos in validPosDir:
                if guarddir in validPosDir[guardpos]:
                    itsaloop = True
                    break

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
            res += 1
            # for pos in obsvisited.keys():
            #     dirs = obsvisited[pos]
            #     if pos not in validPosDir:
            #         validPosDir[pos] = set()
            #     validPosDir[pos].update(dirs)

        # remove temp obstruction
        floormap.remove(obs)

    return res

AoCRunnerAll(6, 'Guard Gallivant', part1, part2)