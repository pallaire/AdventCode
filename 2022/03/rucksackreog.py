
def itemScore(letter):
		if letter >= "a" and letter <= "z":
			return (ord(letter) - ord("a")) + 1
		else:
			return (ord(letter) - ord("A")) + 27

def problem1(lines):
	total = 0
	for aline in lines:
		aline = aline.strip()
		
		l = len(aline)
		if (l&1) == 1:
			print(f"Line NOT even : {aline}")

		half = l >> 1

		first = set()
		second = set()

		for i in range(half):
			first.add(aline[i])
			second.add(aline[half+i])

		intersect = first.intersection(second).pop()
		total += itemScore(intersect)

	print(f"Problem 1 - My total = {total}")


def problem2(lines):
	sets = []
	for aline in lines:
		aline = aline.strip()
		sets.append(set(aline))

	index = 0
	total = 0
	while index < len(sets):

		intersect = sets[index].intersection(sets[index+1], sets[index+2]).pop()
		total += itemScore(intersect)

		index += 3

	print(f"Problem 2 - My total = {total}")


# filename = "day03test01.txt"
filename = "day03data01.txt"
lines = open(filename).readlines()

print(f"2022 Day 03 using file [{filename}]")
problem1(lines)
problem2(lines)