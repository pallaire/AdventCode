
def buildStacks(colCount, lines):
    stacks = [ [] for _ in range(colCount) ]

    for aline in lines:
        ll = len(aline)
        s = 0
        idx = 1

        while idx < ll:
            c = aline[idx]
            if c != " ":
                stacks[s].append(c)
            s += 1
            idx += 4
    return stacks

def preps(lines):
    linesStack = []
    colCount = 0
    stacks = None
    
    for aline in lines:
        # are we at the index line
        if aline[1] == '1':
            colCount = [int(n) for n in aline.split()][-1]
            stacks = buildStacks(colCount, linesStack)
            return stacks
        else:
            linesStack.insert(0, aline)

def problem1(lines, stacks):
    for aline in lines:
        if aline[0] == 'm':
            tokens = aline.split()
            count = int(tokens[1])
            src = int(tokens[3])-1 
            dst = int(tokens[5])-1

            tmp = stacks[src][-count:]
            tmp.reverse()
            stacks[dst] += tmp
            stacks[src] = stacks[src][:-count]
    print("Problem 1 : ", end="")
    for s in stacks:
        print(s[-1], end="")
    print()

def problem2(lines, stacks):
    for aline in lines:
        if aline[0] == 'm':
            tokens = aline.split()
            count = int(tokens[1])
            src = int(tokens[3])-1 
            dst = int(tokens[5])-1

            stacks[dst] += stacks[src][-count:]
            stacks[src] = stacks[src][:-count]
    print("Problem 2 : ", end="")
    for s in stacks:
        print(s[-1], end="")
    print()


day = '05'
#filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"
lines = open(filename).readlines()


print(f"2022 Day {day} using file [{filename}]")

stacks = preps(lines)
problem1(lines, stacks)

stacks = preps(lines)
problem2(lines, stacks)
