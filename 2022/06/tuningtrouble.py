
def problems(problemnumber, signal, markerlen):

	marker = signal[:markerlen]
	idx = markerlen
	signalLen = len(signal)

	while idx < signalLen:
		substr = signal[idx-markerlen:idx]
		s = set(list(substr))

		if len(s) == markerlen:
			print(f"Problem {problemnumber} : start of packet marker position : {idx}")
			return

		idx += 1


day = '06'
#filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"
lines = open(filename).readlines()


print(f"2022 Day {day} using file [{filename}]")

# Tests
# problem1("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
# problem1("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
# problem1("nppdvjthqldpwncqszvftbrmjlhg", 4)
# problem1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)
# problem1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)
problems(1, lines[0], 4)
problems(2, lines[0], 14)
