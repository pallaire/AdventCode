from rich.console import Console
from rich import inspect

def findInMap(amap, target):
	h = len(amap)
	w = len(amap[0])
	for y in range(h):
		for x in range(w):
			if amap[y][x] == target:
				return (x, y)
	return None

def findAllInMap(amap, target):
	allPos = []
	h = len(amap)
	w = len(amap[0])
	for y in range(h):
		for x in range(w):
			if amap[y][x] == target:
				allPos.append((x, y))
	return allPos


def addPositions(p1, p2):
	return (p1[0]+p2[0], p1[1]+p2[1])

def subPositions(p1, p2):
	return (p1[0]-p2[0], p1[1]-p2[1])

def isInMap(w, h, p):
	return not (p[0]<0 or p[1]<0 or p[0]>=w or p[1]>=h)

def isPosInList(alist, pos):
	for l in alist:
		if pos == l.pos:
			return True
	return False

class AStarNode:
	def __init__(self, pos, F, G, H, parent):
		self.pos = pos
		self.F = F
		self.G = G
		self.H = H
		self.parent = parent

	def __eq__(self, other):
		return self.pos == other.pos
	
def printMap(amap, isElevationMap=True):
	h = len(amap)
	w = len(amap[0])
	colorSteps = int(256/26)
	aOrd = ord('a')

	console = Console(color_system='truecolor')

	console.print(f"   ", end='')
	for x in range(w):
		console.print(f"{int(x/10)}", end='')
	console.print()
	console.print(f"   ", end='')
	for x in range(w):
		console.print(f"{int(x%10)}", end='')
	console.print()

	if isElevationMap:
		for y in range(h):
			console.print(f"{y:02} ", end='')
			for x in range(w):
				m = amap[y][x]
				e = ord(m) - aOrd
				c = e*colorSteps
				console.print(m, style=f"rgb({c},{c},{c})", end='')
			console.print(f" {y:02}")
	else:
		for y in range(h):
			console.print(f"{y:02} ", end='')
			for x in range(w):
				m = amap[y][x]
				console.print(m, end='')
			console.print(f" {y:02}")

	console.print(f"   ", end='')
	for x in range(w):
		console.print(f"{int(x/10)}", end='')
	console.print()
	console.print(f"   ", end='')
	for x in range(w):
		console.print(f"{int(x%10)}", end='')
	console.print()

def printPath(w, h, path):
	area = []
	for y in range(h):
		line = []
		for x in range(w):
			line.append(' ')
		area.append(line)

	symbols = {
			( 1,  0):'→', 
			( 0,  1):'↓', 
			(-1,  0):'←', 
			( 0, -1):'↑', 
			( 1,  1):'↘️', 
			( 1, -1):'↗️', 
			(-1,  1):'↙️', 
			(-1, -1):'↖️', 
		}

	pre = path[0]
	for cur in path[1:]:
		dxy = subPositions(cur, pre)
		area[pre[1]][pre[0]] = symbols[dxy]
		pre = cur

	last = path[-1]
	area[last[1]][last[0]] = 'X'

	printMap(area, isElevationMap=False)

	



def AStar(amap, startPos, endPos, skipOnA):
	h = len(amap)
	w = len(amap[1])
	start = AStarNode(startPos, 0, 0, 0, None)
	end = AStarNode(endPos, 0, 0, 0, None)

	openSet = []
	openSet.append(start)

	closeSet = []

	firstNode = True

	while len(openSet) > 0:
		currentNode = min(openSet, key=lambda x: x.F)	
		# print(f"From openSet working with position: {currentNode.pos}")

		if currentNode == end:
			# print('**Reached the end')
			path = []
			n = currentNode
			while n is not None:
				path.append(n.pos)
				n = n.parent

			path.reverse()
			# print(path)
			# printPath(w, h, path)
			# print("Problem 1: ", len(path)-1) # removing the first place
			return path
		
		openSet.remove(currentNode)
		closeSet.append(currentNode)

		currentMapChar = amap[currentNode.pos[1]][currentNode.pos[0]]
		currentElevation = ord(currentMapChar)

		if currentMapChar=='a' and skipOnA==True and firstNode==False:
			continue
		firstNode = False

		for delta in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
			
			newPos = addPositions(currentNode.pos, delta)

			if not isInMap(w, h, newPos):
				# print(f"    child {newPos} is out of bound")
				continue

			if isPosInList(closeSet, newPos):
				# print(f"    child {newPos} is already in the close list")
				continue


			# check elevation
			mapChar = amap[newPos[1]][newPos[0]]
			if mapChar=='a' and skipOnA==True:
				continue

			newElevation = ord(mapChar)
			if newElevation-currentElevation > 1:
				# print(f"    child {newPos} is too high")
				continue



			
			dxy = subPositions(newPos, currentNode.pos)
			newG = currentNode.G + 1
			newH = dxy[0]**2 + dxy[1]**2
			newF = newG + newH

			# check if child as been discovered, and if so 
			# did we just get to it with a shorter path? 
			childInOpen = [o for o in openSet if o.pos == newPos]
			childWasAddedToOpen = False
			if len(childInOpen) > 0:
				# print(f"    child {newPos} was already found, new G is {newG} vs old G {childInOpen[0].G}")
				if newG < childInOpen[0].G:
					# print("        ** Replacing with new G and other values")
					childInOpen[0].G = newG
					childInOpen[0].H = newH
					childInOpen[0].F = newF
					childInOpen[0].parent = currentNode
				childWasAddedToOpen = True

			if not childWasAddedToOpen:
				openSet.append(AStarNode(newPos, newF, newG, newH, currentNode))



def problem1(amap):
	# Find the start and end positions
	# Then replace with the coresponding letters
	startPos = findInMap(amap, 'S')
	amap[startPos[1]] = amap[startPos[1]].replace('S', 'a')

	endPos = findInMap(amap, 'E')
	amap[endPos[1]] = amap[endPos[1]].replace('E', 'z')

	path = AStar(amap, startPos, endPos, False)
	print(f"Problem 1 path length : {len(path)-1}")

def problem2(amap):
	allStartPos = findAllInMap(amap, 'a')
	endPos = findInMap(amap, 'E')
	amap[endPos[1]] = amap[endPos[1]].replace('E', 'z')

	print(allStartPos)
	startCount = len(allStartPos)

	shortestLength = 1000000
	shortestLengthStartPos = None

	for i in range(startCount):
		print(f"{int(i/startCount*100)}%")
		startPos = allStartPos[i]

		path = AStar(amap, startPos, endPos, True)
		if path is not None:
			if len(path) < shortestLength:
				shortestLength = len(path)
				shortestLengthStartPos = startPos

	print(f"Problem 2 path length : {shortestLength-1} from {startPos}")




day = '12'
# filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"

print(f"2022 Day {day} using file [{filename}]")

lines = [aline.strip() for aline in open(filename).readlines()]
problem1(lines)

lines = [aline.strip() for aline in open(filename).readlines()]
problem2(lines)
