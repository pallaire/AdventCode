gearData = {}

def readData(filename):
	with open(filename) as inputfile:
		return inputfile.readlines()
	
def isSymbole(data, w, h, x, y, number):
	global gearData
	if x < 0 or y < 0:
		return False
	if x >= w or y >= h:
		return False
	
	c = data[y][x]
	if c == '.' or c.isdigit():
		return False
	
	if c == "*":
		label = f"{y}-{x}"
		if label in gearData:
			gearData[label].append(number)
		else:
			gearData[label] = [number]
	
	return True

def isSymboleAroundNumber(data, w, h, number, numberEndX, numberEndY):
	numberWidth = len(str(number))
	numberStartX = numberEndX - numberWidth + 1


	if isSymbole(data, w, h, numberStartX-1, numberEndY, number):
		return True

	if isSymbole(data, w, h, numberEndX+1, numberEndY, number):
		return True
	
	for nx in range(numberWidth+2):
		if isSymbole(data, w, h, numberStartX - 1 + nx, numberEndY - 1, number):
			return True

		if isSymbole(data, w, h, numberStartX - 1 + nx, numberEndY + 1, number):
			return True
		
	return False

def parseSchematic(data, getGearData):
	global gearData
	gearData = {}
	total = 0
	h = len(data)
	w = len(data[0])-1

	inNumber = False
	number = 0
	for y in range(h):
		if inNumber:
			# number is over at the end of the line, lets turn around it
			inNumber = False
			if isSymboleAroundNumber(data, w, h, number, w-1, y-1):
				total += number

		for x in range(w):
			c = data[y][x]

			if c.isdigit():
				if inNumber:
					# Continuing number
					number *= 10
					number += int(c)
				else:
					# New number starting
					inNumber = True
					number = int(c)
			else:
				if inNumber:
					# number is over, lets turn around it
					inNumber = False
					if isSymboleAroundNumber(data, w, h, number, x-1, y):
						total += number

	if getGearData:
		gearsDataTotal = 0
		for gears in gearData:
			if len(gearData[gears]) == 2:
				gearsDataTotal += (gearData[gears][0] * gearData[gears][1])
		return gearsDataTotal


	return total


data = readData("large.data")
print(f"Total of the schematics: {parseSchematic(data, False)}")
print(f"Total of the gear data: {parseSchematic(data, True)}")
