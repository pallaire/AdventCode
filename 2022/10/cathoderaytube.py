
def problems(lines):

    cycle = 0
    X = 1

    dump_cycles = [20, 60, 100, 140, 180, 220]
    total = 0

    stdout = []
    for i in range(6):
        stdout.append([' ' for x in range(40)])

    for aline in lines:
        tokens = aline.split()
        command = tokens[0]
        if len(tokens) > 1:
            arg = int(tokens[1])
        else:
            arg = None

        dest_line = int(cycle / 40)
        pos_line = cycle % 40
        if pos_line >= X-1 and pos_line <= X+1:
            stdout[dest_line][pos_line] = '#'


        cycle += 1
        if cycle % 20 == 0:
            if cycle in dump_cycles:
                total += cycle*X            

        if command == 'addx':
            dest_line = int(cycle / 40)
            pos_line = cycle % 40
            if pos_line >= X-1 and pos_line <= X+1:
                stdout[dest_line][pos_line] = '#'

            cycle += 1
            if cycle % 20 == 0:
                if cycle in dump_cycles:
                    total += cycle*X            
            X += arg
            
        
    print(f"Problem 1 signal strength is {total}")
    print(f"Problem 2 message is : ")
    for s in stdout:
        print(''.join(s))


day = '10'
# filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"

lines = [aline.strip() for aline in open(filename).readlines()]

print(f"2022 Day {day} using file [{filename}]")
problems(lines)
