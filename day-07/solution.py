from collections import defaultdict

def canContainShinyGold(bag,inside,seen):
    if bag in seen:
        return False

    seen.add(bag)

    if bag == "shinygoldbag":
        return True
    
    for innerBag,_ in inside[bag]:
        if canContainShinyGold(innerBag,inside,seen):
            return True
    
    return False

def part1(inside):
    res = 0

    for bag in list(inside):
        for innerBag,_ in inside[bag]:
            if canContainShinyGold(innerBag,inside,set()):
                res += 1
                break
        
    return res

def part2(inside):
    for b,_ in inside.items():
        if b == "shinygoldbag":        
            return numOfBagsInside(b,inside)
    
    return -1

def numOfBagsInside(bag,inside):
    res = 0

    for b,c in inside[bag]:
        res += c + c * numOfBagsInside(b,inside)
    
    return res

with open('input-01.txt') as f:
    inside = defaultdict(set)

    for l in f.readlines():
        l = l.rstrip()
        bag,contents = l[:len(l)-1].split(" contain ")
        bag = bag[:len(bag)-1].replace(' ','')
        contents = contents.split(', ')
        
        for content in contents:
            c = ''.join(i for i in content if i != ' ')
            if c[-1] == "s":
                c = c[:len(c)-1]
            
            i = 0
            while c[i].isdigit():
                i += 1
            
            count = 0 if not i else int(c[:i])

            inside[bag].add((c[i:],count))

    print(part1(inside),part2(inside))