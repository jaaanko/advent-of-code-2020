from collections import Counter

def part1(policies):
    res = 0

    for l in policies:
        rule,password = l.split(': ')
        occurences,requiredLetter = rule.split(' ')
        minNum,maxNum = [int(n) for n in occurences.split('-')]

        counts = Counter(password)

        if requiredLetter in counts:
            res += minNum <= counts[requiredLetter] <= maxNum

    return res

def part2(policies):
    res = 0

    for l in policies:
        rule,password = l.split(': ')
        positions,requiredLetter = rule.split(' ')
        pos1,pos2 = [int(n) for n in positions.split('-')]

        if (password[pos1-1] == requiredLetter) ^ (password[pos2-1] == requiredLetter):
            res += 1
            
    return res

with open('input-01.txt') as f:
    policies = f.readlines()
    print(part1(policies),part2(policies))