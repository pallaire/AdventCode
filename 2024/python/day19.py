from aoc import *
import functools

towels = {}
maxtowel = 0


@functools.cache
def recTowelPatternFinder(pattern):
    global towels, maxtowel
    lpat = len(pattern)
    if lpat == 0:
        return 1
    
    for l in range(min(lpat, maxtowel), 0, -1): # start with larger pattern first to go faster
        newpattern = pattern[:l]
        if newpattern in towels[l]:
            res = recTowelPatternFinder(pattern[l:])
            if res == 1:
                return 1
    return 0

@functools.cache
def recTowelPatternFindAll(pattern):
    global towels, maxtowel
    lpat = len(pattern)
    if lpat == 0:
        return 1
    
    res = 0
    for l in range(min(lpat, maxtowel), 0, -1):
        newpattern = pattern[:l]
        if newpattern in towels[l]:
            res += recTowelPatternFindAll(pattern[l:])
    return res


def patternFinder(lines, part):
    global towels, maxtowel
    towelTypes = lines[0].split(', ')
    
    # resetting global and cache
    towels = {}
    maxtowel = 0
    recTowelPatternFinder.cache_clear()
    recTowelPatternFindAll.cache_clear()
    
    for t in towelTypes:
        l = len(t)
        if l not in towels:
            towels[l] = set()
        towels[l].add(t)
        maxtowel = max(maxtowel, l)
        
    res = 0
    for aline in lines[2:]:
        if part == 1:
            res += recTowelPatternFinder(aline)
        else:
            res += recTowelPatternFindAll(aline)
    return res

def part1(lines, istesting):
    return patternFinder(lines, 1)

def part2(lines, istesting):
    return patternFinder(lines, 2)


AoCRunnerAll(19, 'RAM Run', part1, part2)

