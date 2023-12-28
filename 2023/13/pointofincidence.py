def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            res.append(aline.strip())
        return res


def binaryConversion(field):
    colBits = len(field)
    rowBits = len(field[0])

    cols = [0]*rowBits
    rows = [0]*colBits

    for y in range(colBits):
        for x in range(rowBits):
            bit = 1 if field[y][x] == '#' else 0
            rows[y] = (rows[y] << 1) + bit
            cols[x] = (cols[x] << 1) + bit

    return { "cols":cols, "rows":rows }


def findMirror(data, ignore=-1):

    length = len(data)
    delta = None
    start = None

    for i in range(1, length):
        v = data[i]

        if delta == None:
            if data[i-1] == v:
                start = i
                delta = 3
        else:
            if (i-delta) < 0 and start != ignore:
                return start
            
            if data[i-delta] == v:
                delta += 2
            else:
                delta = None
                start = None

    if start != None and start != ignore:
        return start

    return -1

def printField(field):
    h = len(field)
    w = len(field[0])

    for y in range(h):
        for x in range(w):
            print(field[y][x], end='')
        print()

    print()
    print("----------------------------------------")
    print()



def pointofincidenceWithSmudge(data):
    fields = []

    work = []
    for aline in data:
        if not aline:
            fields.append(work)
            work = []
        else:
            work.append(aline)
    fields.append(work)

    res = 0
    idx = 0
    for afield in fields:

        h = len(afield)
        w = len(afield[0])
      
        binaries = binaryConversion(afield)
        rows = binaries["rows"]
        cols = binaries["cols"]

        originalrowsres = findMirror(rows)
        originalcolsres = findMirror(cols)

        afieldres = 0
        
        for y in range(h):
            for x in range(w):

                # flip a bit
                rows[y] = rows[y] ^ (1 << x)
                cols[x] = cols[x] ^ (1 << y)

                rowsres = findMirror(rows, originalrowsres)
                colsres = findMirror(cols, originalcolsres)

                # reset flip a bit
                rows[y] = rows[y] ^ (1 << x)
                cols[x] = cols[x] ^ (1 << y)

                afieldres = 0
                if rowsres != -1 and rowsres != originalrowsres:
                    afieldres += rowsres * 100

                if colsres != -1 and colsres != originalcolsres:
                    afieldres += colsres

                if afieldres != 0:
                    break

            if afieldres != 0:
                break

        print(f"{idx} = {afieldres}")
        idx += 1
        res += afieldres
    return res




def pointofincidence(data):
    fields = []

    work = []
    for aline in data:
        if not aline:
            fields.append(work)
            work = []
        else:
            work.append(aline)
    fields.append(work)

    res = 0
    idx = 0
    for afield in fields:
        binaries = binaryConversion(afield)
        rowsres = findMirror(binaries['rows'])
        colsres = findMirror(binaries['cols'])

        afieldres = 0
        if rowsres != -1:
            afieldres += rowsres * 100

        if colsres != -1:
            afieldres += colsres

        print(f"{idx} = {afieldres}")
        idx += 1
        res += afieldres
    return res

data = readData("/home/pallaire/devs/AdventCode/2023/13/large.data")
print(f"Problem 1 : {pointofincidence(data)}")
print(f"Problem 2 : {pointofincidenceWithSmudge(data)}")
