
filename = "data01.txt"
lines = open(filename).readlines()

# values
# A = rock = X		= 1
# B = paper = Y		= 2
# C = scisor = Z	= 3
#
# loss = 0
# draw = 3
# win = 6


values = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3, }
results = {
	11:0, 	# rock rock = elf draw
	12:-1,	# rock paper = elf lose
	13:1,		# rock scisor = elf win
	21:1,		# paper rock = elf win
	22:0,		# paper paper = elf draw
	23:-1,	# paper scisor = elf lose
	31:-1,	# scisor rock = elf lose
	32:1,		# scisor paper = elf win
	33:0		# scisor scisor = elf draw
}

myscore = 0
elfscore = 0
for l in lines:
	elfhand = values[l[0]]
	myhand = values[l[2]]

	elfscore += elfhand
	myscore += myhand

	elfres = results[elfhand*10 + myhand]

	if elfres == 1:
		elfscore += 6
	elif elfres == -1:
		myscore += 6
	else:
		elfscore += 3
		myscore += 3

print(f"Problem 1 [{filename}] - My score = {myscore}")

# reversed results
# X - I lose
# Y = I draw
# Z = I win

reversedResults = {'X':-1, 'Y':0, 'Z':1}
reversedPlay = {
	-11:3, # lose vs rock = scisor
	-12:1, # lose vs paper = rock
	-13:2, # lose vs scisor = paper

	1:1, # draw vs rock = rock
	2:2, # draw vs paper = paper
	3:3, # draw vs scisor = scisor

	11:2, # win vs rock = paper
	12:3, # win vs paper = scisor
	13:1, # win vs scisor = rock
}

myscore = 0
elfscore = 0
for l in lines:
	elfhand = values[l[0]]
	myWantedresult = reversedResults[l[2]]

	if myWantedresult < 0:
		myhand = reversedPlay[myWantedresult*10-elfhand]
	else:
		myhand = reversedPlay[myWantedresult*10+elfhand]

	elfscore += elfhand
	myscore += myhand

	if myWantedresult == 1:
		myscore += 6
	elif myWantedresult == -1:
		elfscore += 6
	else:
		elfscore += 3
		myscore += 3

print(f"Problem 1 [{filename}] - My score = {myscore}")
