import re
from functools import cmp_to_key

def readData(filename):
	with open(filename) as inputfile:
		return inputfile.readlines()

def parseData(data):
	maps = {}

	seeds = [int(x) for x in re.findall(r"\d+", data[0])]
	maps["theseeds"] = seeds

	name = ""
	numbers = []

	for aline in data[2:]:
		aline = aline.strip()

		if aline == "":
			maps[name] = numbers
			name = ""
			numbers = []
		else:
			if aline[0].isdigit():
				numbers.append([int(x) for x in re.findall(r"\d+", aline)])
			else:
				name = aline.split(" ")[0]

	#add the last data if present
	if name != "" and len(numbers) > 0:
		maps[name] = numbers

	return maps

def followMapping(maps, start, number):
	keys = list(maps.keys())
	source = ""
	destination = ""
	value = -1
	table = None

	for akey in keys:
		if akey.startswith(start):
			tokens = akey.split("-")
			source = tokens[0]
			destination = tokens[-1]
			table = maps[akey]
			break

	for aconversion in table:
		d = aconversion[0]
		s = aconversion[1]
		r = aconversion[2]

		if number >= s and number < (s + r):
			value = d + (number - s)
			break

		if value == -1:
			value = number

	if destination != "location":
		return followMapping(maps, destination, value)
	
	return value

def fertilize(maps):
	res = []

	seeds = maps["theseeds"]
	for aseed in seeds:
		res.append(followMapping(maps, "seed", aseed))
	return min(res)


def sortSeedRanges(a, b):
	if a[0] < b[0]:
		return -1
	elif a[0] > b[0]:
		return 1
	return 0

def sortMappingRanges(a, b):
	if a[1] < b[1]:
		return -1
	elif a[1] > b[1]:
		return 1
	return 0


def applyMapping(sources, mapping):
	res = []

	mapping = sorted(mapping, key=cmp_to_key(sortMappingRanges))						

	while len(sources) > 0:
		asource = sources.pop(0)
		sstart = asource[0]
		send = asource[1]

		mapped = False

		# source smaller than smallest mapping
		# add directly to results
		if send < mapping[0][1]:
			res.append(asource)
		
		# source larger than the largest mapping
		# add directly to results
		elif sstart > (mapping[-1][1] + mapping[-1][2] - 1):
			res.append(asource)

		# source inside mapping ranges, need to check
		else:

			for m in mapping:
				mstart = m[1]
				mend = m[1] + m[2] - 1
				mnewstart = m[0]

				# source range    [0..3]
				# mapping range     [2..5]
				# results
				#                 [01] 			-> unchanged
				#                   [23]		-> mapped
				if sstart < mstart and send > mstart and send <= mend:
					res.append([sstart, mstart-1])
					res.append([mnewstart, mnewstart + send - mstart])
					mapped = True
					break

				# source range        [4...8]
				# mapping range     [2..5]
				# results
				#                     [45] --> remapped
				#                       [6 8] --> insterted back in the source list
				if sstart >= mstart and sstart < mend and send > mend:
					res.append([mnewstart + sstart - mstart, mnewstart + mend - mstart])
					sources.insert(0, [mend+1, send])
					mapped = True
					break

				#  source range       [5 7]
				#  mapping range   [2......9]
				# results
				#                     [5 7] 	--> remapped
				#                  [2 4] [89]	--> dropped
				if sstart >= mstart and send <= mend:
					res.append([mnewstart + sstart - mstart, mnewstart + send - mstart])
					mapped = True
					break

				#  source range   [2......9]
				#  mapping range     [5 7]
				# results
				#                 [2 4] 			--> unchanged
				#                    [5 7]  	--> mapped
				#                       [89]	--> insert back in the sources
				if sstart < mstart and send > mend:
					res.append([sstart, mstart-1])
					res.append([mnewstart, mnewstart + mend - mstart])
					sources.insert(0, [mend+1, send])
					mapped = True
					break				

			if not mapped:
				res.append(asource)

	return res


def createSuperMap(maps):
	seeds = maps["theseeds"]
	sources = []

	for i in range(len(seeds) >> 1):
		start = seeds[i<<1]
		length = seeds[(i<<1)+1]
		sources.append([ start, start + length - 1])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))

	sources = applyMapping(sources, maps["seed-to-soil"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	sources = applyMapping(sources, maps["soil-to-fertilizer"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	sources = applyMapping(sources, maps["fertilizer-to-water"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	sources = applyMapping(sources, maps["water-to-light"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	sources = applyMapping(sources, maps["light-to-temperature"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	sources = applyMapping(sources, maps["temperature-to-humidity"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	sources = applyMapping(sources, maps["humidity-to-location"])
	sources = sorted(sources, key=cmp_to_key(sortSeedRanges))
	
	return sources[0][0]



data = readData("large.data")
maps = parseData(data)

print(f"Fertilize part 1 = {fertilize(maps)}")
print(f"Fertilize part 2 = {createSuperMap(maps)}")
