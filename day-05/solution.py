def part1(passes):
    res = 0

    for p in passes:
        res = max(generateSeatId(p), res)

    return res

def part2(input):
    ids = sorted([generateSeatId(p) for p in passes])

    for i in range(len(ids)-1):
        if ids[i] + 1 != ids[i+1]:
            return ids[i] + 1
    
    return -1

def generateSeatId(sequence):
    left = 0
    right = 127
    i = 0

    while left < right:
        mid = (left+right) // 2
        if sequence[i] == "F":
            right = mid
        else:
            left = mid + 1

        i += 1

    row = left

    left = 0
    right = 7
    i = len(sequence) - 3
    
    while left < right:
        mid = (left+right) // 2

        if sequence[i] == "L":
            right = mid
        else:
            left = mid + 1

        i += 1  

    col = left

    return row * 8 + col

with open('input-01.txt') as f:
    passes = [l.strip() for l in f.readlines()]
    print(part1(passes),part2(passes))