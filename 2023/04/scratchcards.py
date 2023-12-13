import re

def readData(filename):
	with open(filename) as inputfile:
		return inputfile.readlines()


def countWinnings(cards, getTotalCards):
	total = 0

	cardscount = {}

	for acard in cards:
		cardparts = acard.split(":") 
		id = int(re.findall(r"\d+", cardparts[0])[0])
		cardscount[id] = cardscount.get(id, 0) + 1


		subcards = cardparts[1]
		sections = subcards.split("|")
		numbers = re.findall(r"\d+", sections[0])
		winners = re.findall(r"\d+", sections[1])

		winningNumbers = 0
		points = 0
		for n in numbers:
			if n in winners:
				winningNumbers += 1
				if points == 0:
					points = 1
				else:
					points *= 2

		for w in range(winningNumbers):
			cardscount[id + w + 1] = cardscount.get(id + w + 1, 0) + cardscount[id]

		total += points

	if getTotalCards:
		total = 0
		for c in range(len(cards)):
			total += cardscount[c+1]


	return total


data = readData("large.data")
print(f"Part 1: Total points {countWinnings(data, getTotalCards=False)}")

print(f"Part 2: Total cards {countWinnings(data, getTotalCards=True)}")