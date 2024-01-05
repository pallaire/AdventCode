import re

def readData(filename):
    with open(filename) as inputfile:
        lines = inputfile.readlines()
        res = []
        for aline in lines:
            aline = aline.strip()
            if len(aline) > 0:
                res.append(aline)
        return res


def decodeRule(ruletext):
    decodedRule = {}

    (name, rulestext) = re.search(r"(\w+){(.*)}", ruletext).groups()
    rulestokens = rulestext.split(',')
    parttypes = set()
    checks = []
    for r in rulestokens:
        if ':' in r:
            (part, check, value, dest) = re.match(r"(\w)([\<\>])(\d+):(\w+)", r).groups()
            parttypes.add(part)
            checks.append({'part':part, 'check':check, 'value':int(value), 'dest':dest})
        else:
            decodedRule['default'] = r

    decodedRule['name'] = name
    decodedRule['checks'] = checks
    decodedRule['parttypes'] = parttypes

    return decodedRule

def decodePart(parttext):
    part = {}
    attributes = parttext[1:-1].split(',')
    for a in attributes:
        letter = a[0]
        value = int(a[2:])
        part[letter] = value
    return part

def followRules(part, rules, step):
    therule = rules[step]
    terminal = 'AR'
    default = therule['default']

    for c in therule['checks']:
        subvalue = part[c['part']]
        checkvalue = c['value']
        if c['check'] == '>':
            if subvalue > checkvalue:
                if c['dest'] in terminal:
                    return c['dest']
                return followRules(part, rules, c['dest'])
        else:
            if subvalue < checkvalue:
                if c['dest'] in terminal:
                    return c['dest']
                return followRules(part, rules, c['dest'])

    if default=='A' or default=='R':
        return default

    return followRules(part, rules, default)



def filterParts(data):
    parts = []
    rules = {}

    for aline in data:
        if aline[0] == '{':
            # this is a part
            decodedPart = decodePart(aline)
            parts.append(decodedPart)
        else:
            # this is a rule
            decodedRule = decodeRule(aline)
            rules[decodedRule['name']] = decodedRule

    total = 0
    for apart in parts:
        res = followRules(apart, rules, 'in')

        if res == 'A':
            # print(f"Accepted : {apart}")
            total += sum(apart.values())

    return total

def permutePossiblePaths(path):
    mins = {'a':1, 'm':1, 's':1, 'x':1}
    maxs = {'a':4000, 'm':4000, 's':4000, 'x':4000}
    deltas = {'a':0, 'm':0, 's':0, 'x':0}

    for condition in path:
        (name, part, check, value) = condition

        if check == '<':
            maxs[part] = min(maxs[part], value-1)
        elif check == '<=':
            maxs[part] = min(maxs[part], value)
        elif check == '>':
            mins[part] = max(mins[part], value+1)
        elif check == '>=':
            mins[part] = max(mins[part], value)

    # +1 because mins and maxs are inclusive
    deltas['a'] = maxs['a'] - mins['a'] + 1
    deltas['m'] = maxs['m'] - mins['m'] + 1
    deltas['s'] = maxs['s'] - mins['s'] + 1
    deltas['x'] = maxs['x'] - mins['x'] + 1

    res = deltas['a'] * deltas['m'] * deltas['s'] * deltas['x']
    
    # print(f"    {res} from deltas = {deltas}")
    # print()
    # print()

    return res



def followAcceptationPath(rules, currentPath, name):
    arule = rules[name]

    res = 0
    inverts = {'<':'>=', '>':'<='}

    invertedConditions = []
    for subchecks in arule['checks']:
        check = (name, subchecks['part'], subchecks['check'], subchecks['value'])
        invcheck = (name, subchecks['part'], inverts[subchecks['check']],subchecks['value'])

        if subchecks['dest'] != 'R':
            extendedPath = []
            extendedPath += currentPath
            extendedPath += invertedConditions
            extendedPath.append(check)

            if subchecks['dest'] == 'A':
                # print(f"A from check = {extendedPath}")
                res += permutePossiblePaths(extendedPath)
            else:
                res += followAcceptationPath(rules, extendedPath, subchecks['dest'])

        invertedConditions.append(invcheck)

    if arule['default'] != 'R':
        extendedPath = []
        extendedPath += currentPath
        extendedPath += invertedConditions

        if arule['default'] == 'A':
            # print(f"A from default = {extendedPath}")
            res += permutePossiblePaths(extendedPath)
        else:
            res += followAcceptationPath(rules, extendedPath, arule['default'])

    return res



def findAcceptableCombinations(data):
    rules = {}
    for aline in data:
        if aline[0] != '{':
            decodedRule = decodeRule(aline)
            rules[decodedRule['name']] = decodedRule

    return followAcceptationPath(rules, "", "in")


data = readData("large.data")
print(f"Problem 1: {filterParts(data)}")
print(f"Problem 2: {findAcceptableCombinations(data)}")
