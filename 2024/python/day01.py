from aoc import *

def part1(lines):
    left = []
    right = []
    for l in lines:
        (a,b) = [int(x) for x in l.split()]
        left.append(a)
        right.append(b)

    left.sort()
    right.sort()
    return sum(abs(left[i]-right[i]) for i in range(len(left)))

def part2(lines):
    left = []
    right = {}
    for l in lines:
        (a,b) = [int(x) for x in l.split()]
        left.append(a)
        right[b] = right.get(b, 0) + 1
    return sum([right.get(x,0)*x for x in left])

AoCRunnerAll(1, 'Historian Hysteria', part1, part2)
