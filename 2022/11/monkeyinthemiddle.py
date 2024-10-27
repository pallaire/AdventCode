import math
class Monkey:
    def __init__(self, number, lines, item_throw):
        self.number = number
        self.items = []
        self.operation = ''
        self.operation_value = 0
        self.test = 0
        self.true_dest = 0
        self.false_dest = 0
        self.item_throw = item_throw
        self.items_inspected = 0

        for aline in lines:
            if aline.startswith('Starting'):
                text_items = aline[len('Starting items: '):]
                self.items = [int(x) for x in text_items.split(',')]

            elif aline.startswith('Operation'):
                operation = aline[len('Operation: new = '):]
                if operation.startswith('old * old'):
                    self.operation = 'square'
                    self.operation_value = 0
                elif operation.startswith('old + '):
                    opetokens = operation.split('+')
                    self.operation = 'addition'
                    self.operation_value = int(opetokens[1])
                elif operation.startswith('old * '):
                    opetokens = operation.split('*')
                    self.operation = 'multiply'
                    self.operation_value = int(opetokens[1])

            elif aline.startswith('Test'):
                self.test = int(aline[len('Test: divisible by '):])

            elif aline.startswith('If true'):
                self.true_dest = int(aline[len('If true: throw to monkey '):])

            elif aline.startswith('If false'):
                self.false_dest = int(aline[len('If false: throw to monkey '):])

    def add_item(self, item):
        self.items.append(item)

    def inspect(self, worry_division, is_division):
        initial_count = len(self.items)
        for _ in range(initial_count):
            i = self.items.pop(0)

            if self.operation == 'multiply':
                newi = i * self.operation_value
            elif self.operation == 'addition':
                newi = i + self.operation_value
            elif self.operation == 'square':
                newi = i * i

            if is_division:
                newi = int(newi / worry_division)
            else:
                newi = newi % worry_division

            if newi % self.test == 0:
                self.item_throw(self.true_dest, newi)
            else:
                self.item_throw(self.false_dest, newi)
            
            self.items_inspected += 1


    def print(self):
        print(f"Monkey number = {self.number}")
        print(f"   items = {self.items}")
        print(f"   operation = {self.operation}")
        print(f"   test = {self.test}")
        print(f"   true_dest = {self.true_dest}")
        print(f"   false_dest = {self.false_dest}")
        print(f"   items_inspected = {self.items_inspected}")



monkeys = []

def item_throw(dest, item):
    global monkeys
    monkeys[dest].add_item(item)

def problems(lines, problem_id, worry_division, rounds):
    global monkeys

    count = len(lines)
    idx = 0

    test_values = []

    while idx*7 <= count:
        m = Monkey(idx, lines[idx*7:idx*7+7], item_throw)
        test_values.append(m.test)
        monkeys.append(m)
        idx += 1

    if problem_id == 2:
        # lowest common multiple
        worry_division = math.lcm(*test_values)

    for i in range(rounds):
        for m in range(len(monkeys)):
            monkeys[m].inspect(worry_division, problem_id==1)

    inspection_count = [m.items_inspected for m in monkeys]
    inspection_count.sort(reverse=True)
    print(f"Problem {problem_id}: Top 2 inspectors multiplication = {inspection_count[0] * inspection_count[1]}")

    #reset monkeys
    monkeys = []
    


day = '11'
#filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"

lines = [aline.strip() for aline in open(filename).readlines()]

print(f"2022 Day {day} using file [{filename}]")
problems(lines, 1, 3, 20)
problems(lines, 2, 1, 10000)
