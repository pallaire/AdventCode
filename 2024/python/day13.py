from aoc import *
import re

def buttonPermutater(dest, movea, moveb, btna, btnb):
	print(btna, btnb)
	if (movea[0]*btna + moveb[0]*btnb)>dest[0] or (movea[1]*btna + moveb[1]*btnb)>dest[1]:
		return (0xFFFFFFFF, 0xFFFFFFFF) # invalid

	if (movea[0]*btna + moveb[0]*btnb)==dest[0] and (movea[1]*btna + moveb[1]*btnb)==dest[1]:
		return (btna, btnb)

	resb = buttonPermutater(dest, movea, moveb, btna, btnb+1)
	resa = buttonPermutater(dest, movea, moveb, btna+1, btnb)

	if 3*resb[0]+resb[1] < 3*resa[0]+resa[1]:
		return resb
	return resa

def part1(lines):
	llen = len(lines)
	l = 0
	res = 0
	
	# These are linear equations, but resolving them 
	# Button A: X+94, Y+34
	# Button B: X+22, Y+67
	# Prize: X=8400, Y=5400
	
	while l+2 < llen:
		(xa, ya) = [int(x) for x in re.findall("\d+", lines[l+0])]					
		(xb, yb) = [int(x) for x in re.findall("\d+", lines[l+1])]					
		(dx, dy) = [int(x) for x in re.findall("\d+", lines[l+2])]
		l += 4 # we need to skip the blank line as well

		# btnA*xa + btnB*xb = dx
		# btnA*ya + btnB*yb = dy
		
		# with numbers
		# btnA*94 + btnB*22 = 8400
		# btnA*34 + btnB*67 = 5400

		# we need to eliminate a variable, remove btnA firsrt
		# we need to scale the equation
		# so multiply the first formula by the btnA multiplier of the second formula
		# then multiply the second formula by the btnA multiplier of the first formula

		# btnA*94 = 8400 - btnB*22

		# btnA = 8400 - btnB*22
		# 			 --------------
		#              94

		# btnA*34 = 5400 - btnB*67

		# btnA = 5400 - btnB*67
 		# 			 --------------
		#              34

		# 5400 - btnB*67  			 8400 - btnB*22
 		# --------------    =    --------------
		#       34								  	 94

		# 5400*94 - btnB*67*94  = 8400*34 - btnB*22*34

		# 5400*94 - 8400*34 = btnB*67*94 - btnB*22*34
		
		
		# 5400*94 - 8400*34 = btnB
		# -----------------
		#   67*94 - 22*34

		btnB = (dy*xa-dx*ya) / (yb*xa-xb*ya)
		btnA = (dx - btnB*xb) / xa

		if btnA == int(btnA) and btnB == int(btnB):
			res += int(btnA*3 + btnB)

	return res

def part2(lines):
	res = 0
	llen = len(lines)
	l = 0
	res = 0
	
	while l+2 < llen:
		(xa, ya) = [int(x) for x in re.findall("\d+", lines[l+0])]					
		(xb, yb) = [int(x) for x in re.findall("\d+", lines[l+1])]					
		(dx, dy) = [int(x) for x in re.findall("\d+", lines[l+2])]
		l += 4 # we need to skip the blank line as well

		dx += 10000000000000
		dy += 10000000000000

		btnB = (dy*xa-dx*ya) / (yb*xa-xb*ya)
		btnA = (dx - btnB*xb) / xa

		if btnA == int(btnA) and btnB == int(btnB):
			res += int(btnA*3 + btnB)

	return res

AoCRunnerAll(13, 'Garden Groups', part1, part2)
