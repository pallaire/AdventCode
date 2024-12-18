from aoc import *

regA = 0
regB = 0
regC = 0

def combo(operand):
    global regA, regB, regC
    
    match(operand):
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
        case _:
            print(f"ERROR combo invalid operand {operand}")

    
    

def part1(lines):
    global regA, regB, regC

    regA = int(lines[0][12:])
    regB = int(lines[1][12:])
    regC = int(lines[2][12:])
    program = [int(x) for x in lines[4][9:].split(',')]

    inspointer = 0
    tick = 0
    out = ''
    while inspointer < len(program):
        willincrement = True
        opcode = program[inspointer]
        operand = program[inspointer+1]
        
        match(opcode):
            case 0: # adv division
                regA = int(regA / 2**combo(operand))
                
            case 1: # bxl bitwise XOR
                regB = regB ^ operand
                
            case 2: # bst 
                regB = combo(operand) % 8
                
            case 3: # jnz
                if regA != 0:
                    inspointer = operand
                    willincrement = False        
            
            case 4: # bxc
                regB = regB ^ regC
                
            case 5: # out
                tmp = combo(operand)%8
                print(f"{tmp},", end='')
                out += str(tmp)
                
            case 6: # bdv
                regB = int(regA / 2**combo(operand))
                
            case 7: # cdv
                regC = int(regA / 2**combo(operand))
        
        if willincrement:
            inspointer += 2
        tick += 1

    print()
    print(f"{tick} instructions were ran")
    print(f"regA:{regA}  regB:{regB}  regC:{regC}")
    
    return out

def part2(lines):
    res = 0
    return res

AoCRunnerAll(17, 'Chronospatial Computer', part1, part2)

