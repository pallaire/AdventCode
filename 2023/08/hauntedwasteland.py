import re

def readData(filename):
    with open(filename) as inputfile:
        return inputfile.readlines()
    

def followThePath(data):
    instructions = []
    nodes = {}

    lenData = len(data)
    instructions = data[0].strip()

    for i in range(2, lenData):
        tokens = re.findall(r"\w+", data[i].strip())
        nodes[tokens[0]] = [tokens[1], tokens[2]]


    position = "AAA"
    lenInstructions = len(instructions)
    idxInstructions = 0
    count = 0

    while True:
        direction = instructions[idxInstructions]
        idxInstructions = (idxInstructions + 1) % lenInstructions

        if direction == "L":
            position = nodes[position][0]
        else:
            position = nodes[position][1]

        count += 1

        if position == "ZZZ":
            break

    return count


def followThePathFromA(data):
    instructions = []
    nodes = {}

    lenData = len(data)
    instructions = data[0].strip()

    positions = []

    for i in range(2, lenData):
        tokens = re.findall(r"\w+", data[i].strip())
        nodes[tokens[0]] = [tokens[1], tokens[2]]
        
        if tokens[0][2] == "A":
            positions.append(tokens[0])

    timings = []

    for p in positions:
        lenInstructions = len(instructions)
        idxInstructions = 0
        count = 0
        while True:
            direction = instructions[idxInstructions]
            idxInstructions = (idxInstructions + 1) % lenInstructions

            if direction == "L":
                idx = 0
            else:
                idx = 1

            p = nodes[p][idx]

            count += 1

            if p[2] == "Z":
                timings.append(count)
                break

    # This is a LCM ( lowest common multiple ) problem. I found it using a naive approach
    # But this could be solved using prime numbers factorization

    sums = timings.copy()
    sumsCount = len(sums)
    while True:
        maxCount = max(sums)
        converged = 0


        for i in range(len(sums)):
            if sums[i] < maxCount:
                sums[i] += timings[i]

            if sums[i] == maxCount:
                converged += 1

        if converged == sumsCount:
            return maxCount


data = readData("large.data")
print(f"Problem 1 = {followThePath(data)}")
print(f"Problem 2 = {followThePathFromA(data)}")