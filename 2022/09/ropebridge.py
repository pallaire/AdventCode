
def problems(problem_id, lines, tail_count):

	head = [0,0]
	tails = []
	for t in range(tail_count):
		tails.append([0,0])

	visited_positions = set()
	visited_positions.add(tuple(tails[-1]))

	moves = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

	for aline in lines:
		tokens = aline.split()
		direction = tokens[0]
		steps = int(tokens[1])

		for s in range(steps):
			head[0] += moves[direction][0]
			head[1] += moves[direction][1]

			for idx in range(tail_count):
				if idx == 0:
					h = head
				else:
					h = tails[idx-1]
				

				t = tails[idx]

				dx = h[0] - t[0]
				dy = h[1] - t[1]
				adx = abs(dx)
				ady = abs(dy)

				delta = adx+ady

				previous_direction = [0,0]
				if h[0] > t[0]:
					previous_direction[0] = 1
				elif h[0] < t[0]:
					previous_direction[0] = -1

				if h[1] > t[1]:
					previous_direction[1] = 1
				elif h[1] < t[1]:
					previous_direction[1] = -1


				if delta == 4:
					# .....T.
					# .......
					# ..H....
					t[0] = h[0] - previous_direction[0]
					t[1] = h[1] - previous_direction[1]
				elif delta == 3: 
					# .....T.
					# ...H...
					# .......
					if adx > ady:
						t[1] = h[1]
						t[0] = h[0] - previous_direction[0]
					else:
						t[0] = h[0]
						t[1] = h[1] - previous_direction[1]
				if delta == 2:
					#  this         not this
					# .......       ....T..
					# ...H.T.       ...H...
					# .......       .......
					if adx != ady:
						t[0] = h[0] - previous_direction[0]
						t[1] = h[1] - previous_direction[1]

				tails[idx] = t

				if idx == tail_count-1:
					visited_positions.add(tuple(t))

	print(f"Problem {problem_id} number of positions visited by the tail is {len(visited_positions)}")



day = '09'
# filename = f"day{day}test01.txt"
# filename = f"day{day}test02.txt"
filename = f"day{day}data01.txt"

lines = [aline.strip() for aline in open(filename).readlines()]

print(f"2022 Day {day} using file [{filename}]")
problems(1, lines, 1)
problems(2, lines, 9)


