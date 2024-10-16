import re

def problem1(lines):
	totalinclusion = 0
	for aline in lines:
		aline = aline.strip()

		stringnumbers = re.split(r"[,|-]", aline)
		numbers = [int(sn) for sn in stringnumbers]

		if (numbers[0] >= numbers[2] and numbers[1] <= numbers[3]) or (numbers[0] <= numbers[2] and numbers[1] >= numbers[3]):
			totalinclusion += 1

	print(f"Problem 1 - Total inclusions count : {totalinclusion}")

def problem2(lines):
	totalexclusion = 0
	for aline in lines:
		aline = aline.strip()

		stringnumbers = re.split(r"[,|-]", aline)
		numbers = [int(sn) for sn in stringnumbers]

		if numbers[1] < numbers[2] or numbers[3] < numbers[0]:
			totalexclusion += 1

	print(f"Problem 2 - Total overlap count : {len(lines) - totalexclusion}")


# filename = "day04test01.txt"
filename = "day04data01.txt"
lines = open(filename).readlines()

print(f"2022 Day 04 using file [{filename}]")
problem1(lines)
problem2(lines)
