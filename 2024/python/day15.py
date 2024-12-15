from aoc import *

dirs = {'^':(0,-1), '>':(1,0), 'v':(0,1), '<':(-1,0)}

def printMapAndScore(map, rx, ry):
    res = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if x==rx and y==ry:
                print('@', end='')
            else:
                c = map[y][x]
                print(c, end='')
                
                if c == 'O':
                    res += (y*100)+x
                if c == '[':
                    res += (y*100)+x
        print()
    return res

def pushRoundBox(map, x, y, d):
    c = map[y][x]
    
    if c == '#':
        return False
    
    elif c == '.':
        map[y][x] = 'O'
        return True
    else:
        return pushRoundBox(map, x+d[0], y+d[1], d)

def part1(lines):
    map = []
    moves = ''
    
    ismap = True
    for aline in lines:
        if ismap:
            if aline == '':
                ismap = False
            else:
                map.append(list(aline))
        else:
            moves += aline
    
    h = len(map)
    w = len(map[0])
    rx = 0
    ry = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] == '@':
                rx = x
                ry = y
                map[y][x] = '.'
                break
        if rx != 0:
            break

    for m in moves:
        d = dirs[m]
        destx = rx+d[0]
        desty = ry+d[1]
        destchar = map[desty][destx]
        
        if destchar=='#':
            continue
        elif destchar=='.':
            rx = destx
            ry = desty
        else:
            # try to push
            waspushed = pushRoundBox(map, destx, desty, d)
            if waspushed:
                map[desty][destx] = '.'
                rx = destx
                ry = desty
        
    res = printMapAndScore(map, rx, ry)
                
    return res

def pushSquareBox(map, x, y, d, apply):
    c = map[y][x]
    
    if c == '#':
        return False
    
    if d[1] == 0:
        # horizontal push
        if c == '.':
            return True
        else:
            canpush = pushSquareBox(map, x+d[0], y, d, apply)
            if canpush and apply:
                map[y][x+d[0]] = map[y][x]
                map[y][x] = '.'
            return canpush
    else:
        # vertical push
        if c == '.':
            return True

        elif c == ']':
            canpushright = pushSquareBox(map, x, y+d[1], d, apply)
            canpushleft = pushSquareBox(map, x-1, y+d[1], d, apply)
        
            if canpushleft and canpushright and apply:
                # right
                map[y+d[1]][x] = map[y][x]
                map[y][x] = '.'

                # left
                map[y+d[1]][x-1] = map[y][x-1]
                map[y][x-1] = '.'
            return canpushleft and canpushright

        elif c == '[':
            canpushleft = pushSquareBox(map, x, y+d[1], d, apply)
            canpushright = pushSquareBox(map, x+1, y+d[1], d, apply)
        
            if canpushright and canpushleft and apply:
                # left
                map[y+d[1]][x] = map[y][x]
                map[y][x] = '.'

                # right
                map[y+d[1]][x+1] = map[y][x+1]
                map[y][x+1] = '.'
            return canpushleft and canpushright


def part2(lines):
    map = []
    moves = ''
    
    ismap = True
    for aline in lines:
        if ismap:
            if aline == '':
                ismap = False
            else:
                row = []
                for l in aline:
                    if l=='#':
                        row.extend(['#', '#'])
                    elif l == '.':
                        row.extend(['.', '.'])
                    elif l == 'O':
                        row.extend(['[', ']'])
                    else:
                        row.extend(['@', '.'])
                map.append(row)
        else:
            moves += aline
    
    h = len(map)
    w = len(map[0])
    rx = 0
    ry = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] == '@':
                rx = x
                ry = y
                map[y][x] = '.'
                break
        if rx != 0:
            break

    for m in moves:
        d = dirs[m]
        destx = rx+d[0]
        desty = ry+d[1]
        destchar = map[desty][destx]
        
        if destchar=='#':
            continue
        elif destchar=='.':
            rx = destx
            ry = desty
        else:
            # try to push
            canpush = pushSquareBox(map, destx, desty, d, False)
            if canpush:
                pushSquareBox(map, destx, desty, d, True)
                map[desty][destx] = '.'
                rx = destx
                ry = desty
        
    res = printMapAndScore(map, rx, ry)
                
    return res

AoCRunnerAll(15, 'Warehouse Woes', part1, part2)
