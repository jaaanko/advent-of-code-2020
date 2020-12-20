from collections import defaultdict

def isValid(rulesToBeChecked,rulesDict,message):
    if not rulesToBeChecked:
        return not message

    currRuleNum = rulesToBeChecked[0]
    
    if isinstance(rulesDict[currRuleNum],str):
        return message.startswith(rulesDict[currRuleNum]) and isValid(rulesToBeChecked[1:],rulesDict,message[1:])
    
    return any(isValid(ruleNums + rulesToBeChecked[1:],rulesDict,message) for ruleNums in rulesDict[currRuleNum])

def part1(rulesDict,messages):
    return sum(isValid([0],rulesDict,message) for message in messages)

with open('input-01.txt') as f:
    rules, messages = f.read().split('\n\n')
    rulesDict = defaultdict(list)
    messages = messages.split('\n')

    for rule in rules.split('\n'):
        ruleNum, subRuleNums = rule.split(': ')
        ruleNum = int(ruleNum)
        for subRuleNum in subRuleNums.split(' | '):
            if not subRuleNum.split(' ')[0].isdigit():
                rulesDict[ruleNum] = subRuleNum[1:len(subRuleNum)-1]
            else:
                rulesDict[ruleNum].append([int(c) for c in subRuleNum.split(' ')])

    print(part1(rulesDict,messages))
    rulesDict[8].append([42,8])
    rulesDict[11].append([42,11,31])
    print(part1(rulesDict,messages))