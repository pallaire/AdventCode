from aoc import *

def compute(target, value, nums):
    lnums = len(nums)

    if value > target:
        return 0

    pres = value + nums[0]
    if lnums == 1:
        if pres == target:
            return target
    else:
        res = compute(target, pres, nums[1:])
        if res != 0:
            return res

    mres = value * nums[0]
    if lnums == 1:
        if mres == target:
            return target
    else:
        res = compute(target, mres, nums[1:])
        if res != 0:
            return res
    return 0


def computeWithConcat(target, value, nums):
    lnums = len(nums)

    if value > target:
        return 0

    pres = value + nums[0]
    if lnums == 1:
        if pres == target:
            return target
    else:
        res = computeWithConcat(target, pres, nums[1:])
        if res != 0:
            return res

    mres = value * nums[0]
    if lnums == 1:
        if mres == target:
            return target
    else:
        res = computeWithConcat(target, mres, nums[1:])
        if res != 0:
            return res

    cres = int(str(value) + str(nums[0]))
    if lnums == 1:
        if cres == target:
            return target
    else:
        res = computeWithConcat(target, cres, nums[1:])
        if res != 0:
            return res


    return 0

def part1(lines):
    res = 0
    for aline in lines:
        tokens = aline.split(': ')
        target = int(tokens[0])
        nums = [int(x) for x in tokens[1].split(' ')]
        res += compute(target, nums[0], nums[1:])
    return res

def part2(lines):
    res = 0
    for aline in lines:
        tokens = aline.split(': ')
        target = int(tokens[0])
        nums = [int(x) for x in tokens[1].split(' ')]
        compres = computeWithConcat(target, nums[0], nums[1:])
        if compres == target:
            res += target
    return res


AoCRunnerAll(7, 'Bridge Repair', part1, part2)