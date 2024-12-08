from aoc import *
from itertools import combinations

def part1(lines):
    antennas = {}
    antinodes = set()

    h = len(lines)
    w = len(lines[0])

    # Find all the antennas
    for y in range(h):
        for x in range(w):
            a = lines[y][x]
            if a != '.':
                if a in antennas:
                    antennas[a].append((x,y))
                else:
                    antennas[a] = [(x,y)]

    for a in antennas.keys():
        for pair in combinations(antennas[a], 2):
            p1 = pair[0]
            p2 = pair[1]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            anti = (p1[0]-dx, p1[1]-dy)
            if anti[0]>=0 and anti[0]<w and anti[1]>=0 and anti[1]<h:
                antinodes.add(anti)

            anti = (p2[0]+dx, p2[1]+dy)
            if anti[0]>=0 and anti[0]<w and anti[1]>=0 and anti[1]<h:
                antinodes.add(anti)
    return len(antinodes)


def part2(lines):
    antennas = {}
    antinodes = set()
    h = len(lines)
    w = len(lines[0])

    # Find all the antennas
    for y in range(h):
        for x in range(w):
            a = lines[y][x]
            if a != '.':
                if a in antennas:
                    antennas[a].append((x,y))
                else:
                    antennas[a] = [(x,y)]

    for a in antennas.keys():
        for pair in combinations(antennas[a], 2):
            p1 = pair[0]
            p2 = pair[1]

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            tmpantinodes = set()

            step = 1
            x = p1[0] + step
            y = p1[1] + (step*dy/dx)
            while x>=0 and x<w and y>=0 and y<h:
                if(y == int(y)):
                    tmpantinodes.add((x,int(y)))

                step += 1
                x = p1[0] + step
                y = p1[1] + (step*dy/dx)

            step = 1
            x = p1[0] - step
            y = p1[1] - (step*dy/dx)
            while x>=0 and x<w and y>=0 and y<h:
                if(y == int(y)):
                    tmpantinodes.add((x,int(y)))

                step += 1
                x = p1[0] - step
                y = p1[1] - (step*dy/dx)

            tmpantinodes.add(p1)
            tmpantinodes.add(p2)
            antinodes.update(tmpantinodes)

    return len(antinodes)


AoCRunnerAll(8, 'Resonant Collinearity', part1, part2)
