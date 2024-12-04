from aoc import *

def searchAround(lines, w, h, x, y, d, p):
    x += d[0]
    y += d[1]
    p += 1

    if x<0 or x>=w or y<0 or y>=h:
        return 0
    
    c = lines[y][x]
    if c != 'XMAS'[p]:
        return 0
    
    if p==3:
        return 1
    
    return searchAround(lines, w, h, x, y, d, p)

def part1(lines):
    res = 0
    h = len(lines)
    w = len(lines[0])
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    for y in range(h):
        for x in range(w):
            c = lines[y][x]
            if c == 'X':
                for d in dirs:
                    res += searchAround(lines, w, h, x, y, d, 0) 
    return res

def part2(lines):
    res = 0
    h = len(lines)
    w = len(lines[0])
    for y in range(1, h-1):
        for x in range(1, w-1):
            c = lines[y][x]
            if c=='A':
                w1 = lines[y-1][x-1] + lines[y+1][x+1]
                w2 = lines[y-1][x+1] + lines[y+1][x-1]
                if (w1=='MS' or w1=='SM') and (w2=='MS' or w2=='SM'):
                    res += 1
    return res

AoCRunnerAll(4, 'Ceres Search', part1, part2)