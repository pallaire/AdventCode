from aoc import *

def isSafe(report):
    direction = 0
    for i in range(1, len(report)):
        delta = report[i] - report[i-1]
        if delta==0 or abs(delta)>3:
            return 0

        currentdir = 1 if delta>0 else -1
        if direction==0:
            direction = currentdir
        else:
            if currentdir != direction:
                return 0
    return 1     

def part1(lines):
    res = 0
    for l in lines:
        report = [int(x) for x in l.split()]
        res += isSafe(report)
    return res

def part2(lines):
    res = 0
    for l in lines:
        report = [int(x) for x in l.split()]
        if isSafe(report):
            res += 1
        else:
            for i in range(len(report)):
                if isSafe(report[:i] + report[i+1:]):
                    res += 1
                    break
    return res

AoCRunnerAll(2, 'Red-Nosed Reports', part1, part2)