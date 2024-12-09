from aoc import *


def part1(lines):
    line = lines[0]
    res = 0
    fwd = 0
    bck = len(line)-1

    if len(line) & 1 == 0:
        #even line length, skip the last space
        bck -= 1

    defragpos = 0
    backBufferFileLength = 0
    backBufferFileID = 0

    while(fwd <= bck):
        # get file
        filelength = int(line[fwd])
        fileid = int(fwd / 2)
        fwd += 1

        # add value of file to res
        for _ in range(filelength):
            res += defragpos*fileid
            defragpos += 1

        # get the space
        spacelength = int(line[fwd])
        fwd += 1

        # from the back get the last file and add it to a buffer
        # we will take 1 postion of the buffer at a time
        for _ in range(spacelength):
            if backBufferFileLength == 0:
                if bck >= fwd+2:
                    backBufferFileLength = int(line[bck])
                    backBufferFileID = int(bck / 2)
                    bck -= 2

            if backBufferFileLength > 0:
                res += defragpos*backBufferFileID
                defragpos += 1
                backBufferFileLength -= 1
            else:
                # we are done with space at the end
                break
    
    # if the back buffer is not fully emptied, 
    # put the remaining file at the end
    if backBufferFileLength > 0:
        for _ in range(backBufferFileLength):
            res += defragpos*backBufferFileID
            defragpos += 1
            backBufferFileLength -= 1
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
