from aoc import *
import functools

rules = {}

def isvalid(nums):
    seen = set()
    for n in nums:
        if n in rules:
            for r in rules[n]:
                if r in seen:
                    return False
        seen.add(n)
    return True

def compare(a, b):
    if a in rules:
        if b in rules[a]:
            return -1
    elif b in rules:
        if a in rules[b]:
            return 1
    return 0

def updates(lines, reorder):
    global rules

    res = 0
    rules = {}  # clean the global rules
    updates = []

    inrules = True
    for aline in lines:
        aline = aline.strip()
        if aline == '':
            inrules = False
            continue

        if inrules:
            [a,b] = [int(x) for x in aline.split('|')]
            if a in rules:
                rules[a].append(b)
            else:
                rules[a] = [b]
        else:
            updates.append([int(x) for x in aline.split(',')])

    for u in updates:
        if reorder:
            # Part 2
            if isvalid(u) == False:
                sortedu = sorted(u, key=functools.cmp_to_key(compare))
                res += sortedu[(int(len(sortedu)/2))]
        else:
            # Part 1
            if isvalid(u):
                res += u[(int(len(u)/2))]
    return res

def part1(lines):
    return updates(lines, False)

def part2(lines):
    return updates(lines, True)

AoCRunnerAll(5, 'Print Queue', part1, part2)