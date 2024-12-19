from aoc import *
import math

#          N      E      S        W
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
invdirs = {(0,-1):0, (1,0):1, (0,1):2, (-1,0):3}
dirsChar = ['^','>','v','<']

def dijkstra(maze, start, end):
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

            if maze[newy][newx] == '#':
                continue

            newcost = mincost+1
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
                


def part1(lines, istesting):
    if istesting:
        w = 7
        h = 7
        bts = 12
    else:
        w = 71
        h = 71
        bts = 1024
        
    maze = []
    for _ in range(h):
        maze.append(['.']*w)

    for aline in lines[:bts]:
        (x,y) = [int(l) for l in aline.split(',')]
        maze[y][x] = '#'

    dijkstraRes = dijkstra(maze, (0, 0), (w-1, h-1))
    return dijkstraRes['cost']

def part2(lines, istesting):
    if istesting:
        w = 7
        h = 7
        bts = 12
    else:
        w = 71
        h = 71
        bts = 1024
        
    maze = []
    for _ in range(h):
        maze.append(['.']*w)

    for aline in lines[:bts]:
        (x,y) = [int(l) for l in aline.split(',')]
        maze[y][x] = '#'

    dijkstraRes = dijkstra(maze, (0, 0), (w-1, h-1))
    path = dijkstraRes['path']
    
    for aline in lines[bts:]:
        (x,y) = [int(l) for l in aline.split(',')]
        maze[y][x] = '#'
        pos = (x,y)
        if pos in path:
            dijkstraRes = dijkstra(maze, (0, 0), (w-1, h-1))
            if dijkstraRes == None:
                print(f"Breating byte is : {pos}")
                return 0
            path = dijkstraRes['path']

AoCRunnerAll(18, 'RAM Run', part1, part2)

