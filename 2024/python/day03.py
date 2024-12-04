from aoc import *
import re

def part1(lines):
    res = 0
    for l in lines:
        commands = re.findall(r"mul\((\d+,\d+)\)", l)
        for c in commands:
            nums = [int(n) for n in c.split(',')]
            res += nums[0] * nums[1]
    return res

def part2(lines):
    res = 0
    do = True
    for l in lines:
        commands = re.findall(r"mul\((\d+,\d+)\)|(do\(\))|(don't\(\))", l)
        for c in commands:
            c = ''.join(c)
            match c:
                case "do()":
                    do = True
                case "don't()":
                    do = False
                case _ if do==True:
                    nums = [int(n) for n in c.split(',')]
                    res += nums[0] * nums[1]
    return res

AoCRunnerAll(3, 'Mull It Over', part1, part2)