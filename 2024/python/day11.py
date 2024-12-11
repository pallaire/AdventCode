from aoc import *
import functools

@functools.cache
def blink(num, count):
    if count == 0:
        return 1

    if num == 0:
        return blink(1, count-1)

    strnum = str(num)
    lstrnum = len(strnum)
    if lstrnum&1 == 0:
        res = blink(int(strnum[:lstrnum>>1]), count-1)
        res += blink(int(strnum[lstrnum>>1:]), count-1)
        return res

    return blink(num*2024, count-1)

def part1(lines):
    res = 0
    nums = [int(x) for x in lines[0].split()]
    for n in nums: 
        res += blink(n,25)
    return res

def part2(lines):
    res = 0
    nums = [int(x) for x in lines[0].split()]
    for n in nums: 
        res += blink(n,75)
    return res

AoCRunnerAll(11, 'Plutonian Pebbles', part1, part2)
