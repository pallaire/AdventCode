from aoc import *
import sys
import math

sys.setrecursionlimit(12500)

#          N      E      S        W
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
invdirs = {(0,-1):0, (1,0):1, (0,1):2, (-1,0):3}
dirsChar = ['^','>','v','<']

def printPathInMaze(inmaze, path):
    maze = [list(m) for m in inmaze]
    prev = path[0]
    maze[path[0][1]][path[0][0]] = 'S'

    for p in path[1:]:
        dx = p[0] - prev[0]
        dy = p[1] - prev[1]
        cd = invdirs[(dx, dy)]
        maze[p[1]][p[0]] = dirsChar[cd]
        prev = p

    [print(''.join(m)) for m in maze]

def addPositions(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1])

def subPositions(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

def findPosInList(alist, pos):
    for l in alist:
        if l.pos == pos:
            return l
    return None

def indexPosInList(alist, pos):
    for i, l in enumerate(alist):
        if l.pos == pos:
            return i
    return -1

class AStarNode:
    def __init__(self, pos, di, F, G, H, parent):
        self.pos = pos
        self.dir = di
        self.F = F
        self.G = G
        self.H = H
        self.parent = parent

    def __eq__(self, other):
        if type(other) == AStarNode:
            return self.pos == other.pos
        else:
            return self.pos == other
    
    def __str__(self):
        return f"A*  pos:{self.pos} dir:{self.dir} F:{self.F} G:{self.G} H:{self.H} "

def AStar(amap, startPos, endPos):
    start = AStarNode(startPos, 1, 0, 0, 0, None)
    end = AStarNode(endPos, 0, 0, 0, 0, None)

    openSet = []
    openSet.append(start)
    closeSet = []

    while len(openSet) > 0:
        currentNode = min(openSet, key=lambda x: x.F)	

        if currentNode == end:
            path = []
            n = currentNode
            while n is not None:
                path.append(n.pos)
                n = n.parent
            path.reverse()
            return {'cost': currentNode.G, 'path':path}
        
        openSet.remove(currentNode)
        closeSet.append(currentNode)

        for d in range(4): # for each direction
            newDir = (currentNode.dir + d)%4
            delta = dirs[newDir]
            
            newPos = addPositions(currentNode.pos, delta)

            if amap[newPos[1]][newPos[0]] == '#':
                continue

            if findPosInList(closeSet, newPos) != None:
                continue
            
            changeMoveAndDirCost = 1
            if d != 0:   
                # make it expensive to turn
                changeMoveAndDirCost = 1001

            newG = currentNode.G + changeMoveAndDirCost
            dxy = subPositions(newPos, endPos)
            newH = abs(dxy[0]) + abs(dxy[1])
            newF = newG + newH

            # check if child as been discovered, and if so 
            # did we just get to it with a shorter path? 
            foundIdx = indexPosInList(openSet, newPos)
            if foundIdx != -1:
                if newG < openSet[foundIdx].G:
                    del openSet[foundIdx]

            openSet.append(AStarNode(newPos, newDir, newF, newG, newH, currentNode))
    print("ERROR AStar didn't find the end")

def dijkstra(maze, start, end):
    h = len(maze)
    w = len(maze[0])

    ex = end[0]
    ey = end[1]

    # 1D arrays are faster and simpler for this problem
    mazecost = [math.inf] * (w*h)
    mazeprev = [0] * (w*h)
    mazedir = [0xff] * (w*h)
    unvisited = set()
    visited = set()

    startidx = start[0] + (start[1]*w)
    endidx = end[0] + (end[1]*w)

    unvisited.add(startidx)
    mazecost[startidx] = 0
    mazedir[startidx] = 1
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
            break

        x = minidx % w
        y = minidx // w
        dr = mazedir[minidx]

        # if x==ex and y==ey:
        if minidx == endidx:
            print(f"Found it with cost: {mincost}")
            idx = minidx
            path = [(idx%w, idx//w)]
            while idx != startidx:
                idx = mazeprev[idx]                
                path.append((idx%w, idx//w))
            path.reverse()
            return {'cost': mincost, 'path':path}

        unvisited.remove(minidx)
        visited.add(minidx)

        for d in [0, 1, -1]:
            newd = (dr + 4 - d)%4
            delta = dirs[newd]
            newx = x + delta[0]
            newy = y + delta[1]
            newidx = newx + (newy*w)

            if newidx in visited:
                continue

            if maze[newy][newx] == '#':
                continue

            if d == 0:
                newcost = mincost+1
            else:
                newcost = mincost+1001

            if newidx in unvisited:
                if mazecost[newidx] > newcost:
                    mazecost[newidx] = newcost
                    mazeprev[newidx] = minidx
                    mazedir[newidx] = newd
            else:
                unvisited.add(newidx)
                mazecost[newidx] = newcost
                mazeprev[newidx] = minidx
                mazedir[newidx] = newd


def part1(lines):
    global mincost
    h = len(lines)
    w = len(lines[0])
    sx = 1
    sy = h - 2
    ex = w - 2
    ey = 1

    # astarRes = AStar(lines, (sx, sy), (ex, ey))
    dijkstraRes = dijkstra(lines, (sx, sy), (ex, ey))

    return dijkstraRes['cost']

def part2(lines):
    res = 0
    return res

AoCRunnerAll(16, 'Reindeer Maze', part1, part2)

