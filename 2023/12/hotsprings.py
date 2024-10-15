import functools
import re

def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append(aline.strip())
        return res


@functools.cache
def count(pattern, groups):

	# early exits, out of groups
	if not groups:
		if not '#' in pattern:
			return 1
		else:
			return 0
		
	# out of patterns
	if not pattern:
		return 0

	currentPattern = pattern[0]
	currentGroup = groups[0]

	if currentPattern == '#':
		# take the currentGroup length from the pattern
		testPattern = pattern[:currentGroup]
		testPattern = testPattern.replace('?', '#')

		# check if the current group CANT fit in the test pattern
		if testPattern != currentGroup * '#':
			return 0
		
		# so current group can fit here
		# is this the last group?
		if len(pattern) == currentGroup:
			if len(groups) == 1:
				return 1
			else:
				# there is 1 or more groups but the pattern is over
				return 0
		
		# there is more pattern and more groups ... can we make it work? 
		# this is taking the next char after the current group length
		if pattern[currentGroup] in "?.":
			return count(pattern[currentGroup+1:], groups[1:])
	
		# next char wasn´t or couldn´t be a separator
		return 0	
	elif currentPattern == '.':
		return count(pattern[1:], groups)
	elif currentPattern == '?':
		jokercount = count("."+pattern[1:], groups)
		jokercount += count("#"+pattern[1:], groups)
		return jokercount


def hotsprings(data, unfold):
	res = 0

	lineCount = 0

	for aline in data:

		pattern = aline.split(' ')[0]
		groups = [int(x) for x in re.findall("\d+", aline)]

		if unfold:
			unfoldedPattern = ""
			unfoldedGroups = []

			for i in range(5):
				unfoldedPattern += pattern
				if i < 4:
					unfoldedPattern += "?"

				unfoldedGroups = unfoldedGroups + groups
			
			pattern = unfoldedPattern
			groups = unfoldedGroups

		lineres = count(pattern, tuple(groups))

		print(f"Line #{lineCount} = done, with {lineres}")
		res += lineres
		lineCount += 1

	return res

data = readData("large.data")

print(f"Problem 1 = {hotsprings(data, False)}")
print(f"Problem 2 = {hotsprings(data, True)}")


