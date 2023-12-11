import re

def translateDigits(d):
	reference = {	
		'one': 1,
		'two': 2,
		'three': 3,
		'four': 4,
		'five': 5,
		'six': 6,
		'seven': 7,
		'eight': 8,
		'nine': 9,
		'zero': 0,
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
		'0': 0,
	}
	return reference[d]

def filterCalibrationValues(lines, useWords):
	res = 0
	for aline in lines:
		if useWords:
			digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", aline)
		else:
			digits = re.findall("\d", aline)

		if len(digits) > 0:
			number = translateDigits(digits[0])*10 + translateDigits(digits[-1])
			res += number
	return res

def readCalibrationFile(filename):
	with open(filename) as inputfile:
		return inputfile.readlines()

lines = readCalibrationFile('large.data')
res = filterCalibrationValues(lines, False)
print(f"Total of calibration, Part 1 = {res}")

res = filterCalibrationValues(lines, True)
print(f"Total of calibration, Part 2 = {res}")
