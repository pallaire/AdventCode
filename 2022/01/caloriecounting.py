
def problem1(lines):
    totals = []
    subtotal = 0
    for aline in lines:
        if aline == '':
            totals.append(subtotal)
            subtotal = 0;
        else:
            subtotal += int(aline)

    totals.append(subtotal)
    totals.sort()

    print(f"Problem 1 - Most calories  : {totals[-1]}")
    print(f"Problem 2 - Most calories  : {totals[-1] + totals[-2] + totals[-3]}")



# filename = "day01test01.txt"
filename = "day01data01.txt"
lines = [aline.strip() for aline in open(filename).readlines()]

print(f"2022 Day 01 using file [{filename}]")
problem1(lines)
