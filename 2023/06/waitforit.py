import re
import math

# Distance equation
# d = vt + ½*a*t²
#
# v = 0
# d = ½*a*t²
# 2d = a*t²
# a = 2d/t²

def readData(filename):
	with open(filename) as inputfile:
		return inputfile.readlines()


def countWinningSolutions(data):
    res = 0

    times = [int(t) for t in re.findall(r"\d+", data[0])]
    distances = [int(d) for d in re.findall(r"\d+", data[1])]
    races = len(times)

    for r in range(races):
        atime = times[r]
        adistance = distances[r]

        count = 0
        started = False

        for a in range(1, atime):
            remainingTime = atime - a
            testDistance = a * remainingTime
            # print(f"Test d = {testDistance}")

            if testDistance > adistance:
                started = True
                count += 1
            else:
                if started:
                    break

        if res == 0:
             res = count
        else:
             res = res * count
    return res

def countWinningSolutionsForHugeRace(data):
    res = 0

    time = [int(t) for t in re.findall(r"\d+", data[0].replace(" ", ""))][0]
    distance = [int(d) for d in re.findall(r"\d+", data[1].replace(" ", ""))][0]
    #time = 10
    #distance = 15

    for a in range(time>>1):
        rt = time - a
        if a*rt > distance:
            print(f"found start = {a} with remaining time = {rt}")
            return rt - a + 1
            

        if a % 10000 == 0:
            print(a)

    return -1

data = readData("large.data")
print(f"Problem 1 - winnings count = {countWinningSolutions(data)}")
print(f"Problem 2 - winnings count = {countWinningSolutionsForHugeRace(data)}")


# t = 10
# d = 15
# 1 9 = 9
# 2 8 = 16
# 3 7 = 21
# 4 6 = 24
# 5 5 = 25
# 6 4 = 24
# 7 3 = 21
# 8 2 = 16
# 9 1 = 9


