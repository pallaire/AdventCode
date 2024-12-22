from aoc import *
import math

#          N      E      S        W
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
invdirs = {(0,-1):0, (1,0):1, (0,1):2, (-1,0):3}
dirsChar = ['^','>','v','<']

def dijkstra(maze, start, end, maxcost, cheats):
    h = len(maze)
    w = len(maze[0])

    # 1D arrays are faster and simpler for this problem
    mazecost = [math.inf] * (w*h)
    mazeprev = [0] * (w*h)
    unvisited = set()
    visited = set()

    startidx = start[0] + (start[1]*w)
    endidx = end[0] + (end[1]*w)

    unvisited.add(startidx)
    mazecost[startidx] = 0
    mazeprev[startidx] = startidx
  
    while True:
        mincost = math.inf
        minidx = None
        for idx in unvisited:
            if mazecost[idx] < mincost:
                mincost = mazecost[idx]
                minidx = idx

        if minidx == None:
            print("ERROR no unvisited tile to work with")
            return None

        x = minidx % w
        y = minidx // w

        if minidx == endidx:
            idx = minidx
            path = [(idx%w, idx//w)]
            while idx != startidx:
                idx = mazeprev[idx]                
                path.append((idx%w, idx//w))
            path.reverse()
            return {'cost': mincost, 'path':path}

        unvisited.remove(minidx)
        visited.add(minidx)

        for delta in dirs:
            newx = x + delta[0]
            newy = y + delta[1]
            
            if newx<0 or newx>=w or newy<0 or newy>=h:
                continue

            newpos = (newx, newy)
            if newpos not in cheats:
                if maze[newy][newx] == '#':
                    continue

            newcost = mincost+1
            if maxcost!=-1 and newcost>=maxcost:
                continue
            
            newidx = newx + (newy*w)
            if newidx in visited:
                continue

            if newidx in unvisited:
                if mazecost[newidx] > newcost:
                    mazecost[newidx] = newcost
                    mazeprev[newidx] = minidx
            else:
                unvisited.add(newidx)
                mazecost[newidx] = newcost
                mazeprev[newidx] = minidx
                
def printPath(w, h, path):
    area = []
    for y in range(h):
        area.append([' ']*w)
        
    for p in path:
        area[p[1]][p[0]] = 'O'
        
    for y in range(h):
        for x in range(w):
            print(area[y][x], end='')
        print()

def part1(lines, istesting):
    h = len(lines)
    w = len(lines[0])
    
    start = None
    end = None
    
    for y in range(h):
        for x in range(w):
            c = lines[y][x]
            if c == 'S':
                start = (x,y)
            elif c == 'E':
                end = (x,y)
    
    cheats = set()
    dijkstraRes = dijkstra(lines, start, end, -1, cheats)
    maxcost = dijkstraRes['cost']
    pathdict = {}
    for i,p in enumerate(dijkstraRes['path']):
        pathdict[p] = i
    
    print(f"maxcost: {maxcost}, path length: {len(dijkstraRes['path'])}")
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    res = 0
    
    for p in dijkstraRes['path']:
        for d in dirs:
            cheatwall = (p[0]+d[0], p[1]+d[1]) 
            cheatpos = (p[0]+d[0]*2, p[1]+d[1]*2)
            if (cheatwall not in pathdict) and (cheatpos in pathdict):
                if pathdict[cheatpos]-pathdict[p]-2 >= 100: # -2 is for the wall crossing
                    res += 1
    return res

def part2(lines, istesting):
    return 0

AoCRunnerAll(20, 'Race Condition', part1, part2)

