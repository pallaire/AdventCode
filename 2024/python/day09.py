from aoc import *


def part1(lines):
    line = lines[0]
    lline = len(line)

    res = 0

    fwd = 0
    bck = lline-1
    if lline & 1 == 0:
        #even line length, skip the last space
        bck -= 1

    defragpos = 0

    bbufferfilelength = 0
    bbufferfileid = 0

    while(fwd <= bck):
        # get file
        filelength = int(line[fwd])
        fileid = int(fwd / 2)
        fwd += 1

        for i in range(filelength):
            res += defragpos*fileid
            defragpos += 1

        #get the space
        spacelength = int(line[fwd])
        fwd += 1

        for s in range(spacelength):
            if bbufferfilelength == 0:
                if bck >= fwd+2:
                    bbufferfilelength = int(line[bck])
                    bbufferfileid = int(bck / 2)
                    bck -= 2

            if bbufferfilelength > 0:
                res += defragpos*bbufferfileid
                defragpos += 1
                bbufferfilelength -= 1
            else:
                # we are done with space at the end
                break
    
    if bbufferfilelength > 0:
        for b in range(bbufferfilelength):
            res += defragpos*bbufferfileid
            defragpos += 1
            bbufferfilelength -= 1

    return res

def part2(lines):
    line = lines[0]

    chunks = []
    for (idx, c) in enumerate(line):
        i = int(c)
        isfile = (idx&1 == 0)

                    # file/space   id    len
        chunks.append((isfile, int(idx/2), i))

    # 00...111...2...333.44.5555.6666.777.888899
    # 0099.111...2...333.44.5555.6666.777.8888..
    # 0099.1117772...333.44.5555.6666.....8888..
    # 0099.111777244.333....5555.6666.....8888..
    # 00992111777.44.333....5555.6666.....8888..        
    spaceidx = 1
    smallesthole = 1
    while spaceidx < len(chunks):
        isfile = chunks[spaceidx][0]
        if isfile:
            spaceidx += 1
            continue

        spacelen = chunks[spaceidx][2]

        if spacelen < smallesthole:
            spaceidx += 1
            continue

        matchidx = -1
        smallestfound = 11
        for bidx in range(len(chunks)-1, 0, -1):
            isfile = chunks[bidx][0]
            if not isfile:
                continue

            if bidx <= spaceidx:
                break

            filelen = chunks[bidx][2]
            smallestfound = min(smallestfound, filelen)
            if filelen <= spacelen:
                matchidx = bidx
                break
        
        if matchidx > 0:
            fileid = chunks[matchidx][1]
            filelen = chunks[matchidx][2]
            if filelen == spacelen:
                chunks[spaceidx] = (True, fileid, filelen)
                chunks[matchidx] = (False, -1, filelen)
            else:
                # mark back file as space
                chunks[matchidx] = (False, -1, filelen)

                # update remaining space
                chunks[spaceidx] = (False, -1, spacelen-filelen)

                # insert file in hole
                chunks.insert(spaceidx, (True, fileid, filelen))
                spaceidx += 1
        else:
            smallesthole = smallestfound
            spaceidx += 1

    res = 0
    idx = 0
    for c in chunks:
        isfile = c[0]
        cid = c[1]
        clen = c[2]

        for ci in range(clen):
            if isfile:
                res += idx*cid
            idx += 1

    return res


AoCRunnerAll(9, 'Disk Fragmenter', part1, part2)
