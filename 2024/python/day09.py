from aoc import *


def part1(lines):
    line = lines[0]
    disk = []
    id = 0
    for i, c in enumerate(line):
        if i&1 == 0:
            disk.extend([id]*int(c))
            id += 1
        else:
            disk.extend(['.']*int(c))

    res = 0
    idx = 0
    while True:
        if disk[0] != '.':
            res += disk.pop(0)*idx
            idx += 1
            if len(disk) == 0:
                break
        if disk[-1] == '.':
            disk.pop()
            if len(disk) == 0:
                break
        if disk[0]=='.' and disk[-1]!='.':
            res += disk.pop()*idx
            disk.pop(0)
            idx += 1
        if len(disk) == 0:
            break

    return res


def part2(lines):
    line = lines[0]

    chunks = []
    for (idx, c) in enumerate(line):
        i = int(c)
        chunks.append((int(idx/2) if (idx&1 == 0) else -1, i))

    spaceidx = 1
    smallesthole = 1
    while spaceidx < len(chunks):
        isfile = chunks[spaceidx][0] >= 0
        if isfile:
            spaceidx += 1
            continue

        spacelen = chunks[spaceidx][1]

        if spacelen < smallesthole:
            spaceidx += 1
            continue

        matchidx = -1
        smallestfound = 11
        for bidx in range(len(chunks)-1, 0, -1):
            isfile = chunks[bidx][0] >= 0
            if not isfile:
                continue

            if bidx <= spaceidx:
                break

            filelen = chunks[bidx][1]
            smallestfound = min(smallestfound, filelen)
            if filelen <= spacelen:
                matchidx = bidx
                break
        
        if matchidx > 0:
            fileid = chunks[matchidx][0]
            filelen = chunks[matchidx][1]
            if filelen == spacelen:
                # replace space with match
                chunks[spaceidx] = chunks[matchidx]

                # update match to empty
                chunks[matchidx] = (-1, filelen)
            else:
                # mark back file as space
                chunks[matchidx] = (-1, filelen)

                # update remaining space
                chunks[spaceidx] = (-1, spacelen-filelen)

                # insert file in hole
                chunks.insert(spaceidx, (fileid, filelen))
                spaceidx += 1
        else:
            smallesthole = smallestfound
            spaceidx += 1

    res = 0
    idx = 0
    for c in chunks:
        for _ in range(c[1]):
            if c[0] >= 0:
                res += idx*c[0]
            idx += 1
    return res


AoCRunnerAll(9, 'Disk Fragmenter', part1, part2)
