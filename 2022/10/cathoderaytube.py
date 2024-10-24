
def problems(problem_id, lines):

    cycle = 0
    X = 1

    dump_cycles = [20, 60, 100, 140, 180, 220]
    total = 0

    for aline in lines:
        tokens = aline.split()
        command = tokens[0]
        if len(tokens) > 1:
            arg = int(tokens[1])
        else:
            arg = None

        cycle += 1
        if cycle % 20 == 0:
            if cycle in dump_cycles:
                total += cycle*X            
                print(f"1. {command} Cycle={cycle} adding={cycle}x{X}, total={total}")

        if command == 'addx':
            cycle += 1
            if cycle % 20 == 0:
                if cycle in dump_cycles:
                    total += cycle*X            
                    print(f"2. {command}@{arg} Cycle={cycle} adding={cycle}x{X}, total={total}")
            X += arg
            
        
    print(f"Problem {problem_id} signal strength is {total}")

day = '10'
# filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"

lines = [aline.strip() for aline in open(filename).readlines()]

print(f"2022 Day {day} using file [{filename}]")
problems(1, lines)
