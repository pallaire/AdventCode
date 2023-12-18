from functools import reduce
import re

def readData(filename):
    with open(filename) as inputfile:
        return inputfile.readlines()

def getListOfDiffs(data):
    res = []
    for i in range(1, len(data)):
        res.append(data[i] - data[i-1])
    return res


def predictions(data):
    sumsOfPredictions = 0

    for aline in data:
        sequences = [[int(x) for x in re.findall(r"-?\d+", aline)]]

        while True:
            diffs = getListOfDiffs(sequences[-1])
            sequences.append(diffs)

            isDone = True
            for d in diffs:
                if d != 0:
                    isDone = False
                    break

            if isDone:
                break

        sequencesCount = len(sequences)
        for i in range(sequencesCount - 2, -1, -1):
            diffToAdd = sequences[i+1][-1]
            addTo = sequences[i][-1]
            sequences[i].append(addTo + diffToAdd)

        sumsOfPredictions += sequences[0][-1]

    return sumsOfPredictions


def predictionsReverse(data):
    sumsOfPredictions = 0

    for aline in data:
        sequences = [[int(x) for x in re.findall(r"-?\d+", aline)]]

        while True:
            diffs = getListOfDiffs(sequences[-1])
            sequences.append(diffs)

            isDone = True
            for d in diffs:
                if d != 0:
                    isDone = False
                    break

            if isDone:
                break

        sequencesCount = len(sequences)
        for i in range(sequencesCount - 2, -1, -1):
            diffToSub = sequences[i+1][0]
            subFrom = sequences[i][0]
            sequences[i].insert(0, subFrom - diffToSub)
        sumsOfPredictions += sequences[0][0]

    return sumsOfPredictions


data = readData("large.data")
print(f"Problem 1 sums of predictions = {predictions(data)}")
print(f"Problem 2 sums of predictions = {predictionsReverse(data)}")
