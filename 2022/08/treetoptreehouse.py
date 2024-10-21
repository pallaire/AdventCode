def printMap(map):
	for aline in map:
			print(aline)

def problem1(map):
	h = len(map)
	w = len(map[0])

	visible = set()

	# check each line from left to right
	for y in range(1, h-1):
		th = map[y][0]
		for x in range(1, w-1):
			cth = map[y][x]
			if cth > th:
				visible.add((x,y))
				th = cth

	# # check each line from right to left
	for y in range(1, h-1):
		th = map[y][w-1]
		for x in range(w-2, 0, -1):
			cth = map[y][x]
			if cth > th:
				visible.add((x,y))
				th = cth

	# # check each line from top to bottom
	for x in range(1, w-1):
		th = map[0][x]
		for y in range(1, h-1):
			cth = map[y][x]
			if cth > th:
				visible.add((x,y))
				th = cth

	# # check each line from bottom to top
	for x in range(1, w-1):
		th = map[h-1][x]
		for y in range(h-2, 0, -1):
			cth = map[y][x]
			if cth > th:
				visible.add((x,y))
				th = cth

	visiblePerimeter = 2*w + 2*h - 4
	print(f"Problem 1 the number of visible trees is {len(visible) + visiblePerimeter}")

def checkLineOfTree(map, stopHeight, x, y, dx, dy, w, h):
	if x<0 or y<0 or x>=w or y>=h:
		return 0
	
	if map[y][x] >= stopHeight:
		return 1
	
	return 1 + checkLineOfTree(map, stopHeight, x+dx, y+dy, dx, dy, w, h)
	

def problem2(map):
	h = len(map)
	w = len(map[0])
	maxTreeView = 0

	for y in range(h):
		for x in range(w):
			stopHeight = map[y][x]
			treeViewUp    = checkLineOfTree(map, stopHeight, x,   y-1,  0, -1, w, h)
			treeViewDown  = checkLineOfTree(map, stopHeight, x,   y+1,  0,  1, w, h)
			treeViewLeft  = checkLineOfTree(map, stopHeight, x-1, y,   -1,  0, w, h)
			treeViewRight = checkLineOfTree(map, stopHeight, x+1, y,    1,  0, w, h)

			count = treeViewUp * treeViewDown * treeViewLeft * treeViewRight
			if count > maxTreeView:
				maxTreeView = count

	print(f"Problem 2 the maximum of tree view is {maxTreeView}")

day = '08'
#filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"

lines = [aline.strip() for aline in open(filename).readlines()]
map = []
for aline in lines:
	arrayofint = [int(c) for c in list(aline)]
	map.append(arrayofint)

print(f"2022 Day {day} using file [{filename}]")
problem1(map)
problem2(map)
