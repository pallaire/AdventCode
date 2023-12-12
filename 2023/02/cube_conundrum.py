import re

def readGamesData(filename):
	with open(filename) as inputfile:
		return inputfile.readlines()
	
def parseForPossibleGames(games, maxes, getMinimumsPowers):
	validGamesIDTotal = 0
	minimumsPowerTotal = 0
	
	for agame in games:
		gameID = int(re.findall(r"^Game (\d+):", agame)[0])
		minimums = {'blue':0, 'green':0, 'red':0 }
		valid = True

		sets = agame.split(";")

		for aset in sets:
			colors = re.findall(r"(\d+)\s(blue|red|green)", aset)

			for acolor in colors: 
				colourCount = int(acolor[0])
				colorName = acolor[1]

				if colourCount > maxes[colorName]:
					valid = False

				if colourCount > minimums[colorName]:
					minimums[colorName] = colourCount
		
		if valid:
			validGamesIDTotal += gameID

		minimumsPowerTotal += (minimums['blue'] * minimums['green'] * minimums['red'])

	if getMinimumsPowers:
		return minimumsPowerTotal
	return validGamesIDTotal	
	

gameslines = readGamesData("large.data")
print(f"Possible games total: {parseForPossibleGames(gameslines, {'blue':14, 'green':13, 'red': 12 }, getMinimumsPowers=False)}")

print(f"Possible minimum game power total: {parseForPossibleGames(gameslines, {'blue':14, 'green':13, 'red': 12 }, getMinimumsPowers=True)}")