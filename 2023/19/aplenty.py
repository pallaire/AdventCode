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

    print(parts)

    total = 0
    for apart in parts:
        res = followRules(apart, rules, 'in')

        if res == 'A':
            print(f"Accepted : {apart}")
            total += sum(apart.values())
        else:
            print(f"Rejected : {apart}")

    return total

def findAcceptableCombinations(data):
    rules = {}
    for aline in data:
        if aline[0] != '{':
            decodedRule = decodeRule(aline)
            rules[decodedRule['name']] = decodedRule

    defaultAccept = []
    defaultReject = []
    checksToAccept = []
    checksToReject = []
    rulesNames = set(rules.keys())
    rulesDests = set()

    for arulekey in rules:
        arule = rules[arulekey]
        for subchecks in arule['checks']:
            if subchecks['dest'] != 'A' and subchecks['dest'] != 'R':
                rulesDests.add(subchecks['dest'])

    if len(rulesDests) != len(rulesNames):
        print(f"Rules without dest??? dests:{len(rulesDests)}   rules:{len(rulesNames)}")

    validRulesNames = set()
    validRulesNames.add('in')
    for rulename in rulesNames:
        if (rulename in rulesDests or rulename=="in") and rulename!='A' and rulename!='R':
            validRulesNames.add(rulename)

    for arulekey in rules:
        arule = rules[arulekey]

        default = arule['default']
        if default == 'A':
            defaultAccept.append(arule)
        elif default == 'R':
            defaultReject.append(arule)

    print(f"dests:{len(rulesDests)}   rules:{len(validRulesNames)}")
    print(sorted(rulesDests))
    print(sorted(validRulesNames))

            

    


data = readData("large.data")
# print(f"Problem 1: {filterParts(data)}")
print(f"Problem 2: {findAcceptableCombinations(data)}")