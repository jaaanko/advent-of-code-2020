def getRotationResult(currFace,direction,degree):
    dirs = 'ESWN'
    i = degree//90

    if direction == 'L':
        i = -i
    
    return dirs[(dirs.index(currFace) + i) % 4]

def getManhattanDist(ship):
    return abs(ship['N']-ship['S']) + abs(ship['E']-ship['W'])

def part1(instructions):
    currFace = 'E'
    ship = {'N':0,'S':0,'E':0,'W':0}

    for ins,v in instructions:
        if ins == 'F':
            ship[currFace] += v    
        elif ins == 'L' or ins == 'R':
            currFace = getRotationResult(currFace,ins,v)
        else:
            ship[ins] += v

    return getManhattanDist(ship)

def part2(instructions):
    ship = {'N':0,'S':0,'E':0,'W':0}
    waypoint = {'N':1,'S':0,'E':10,'W':0}

    for ins,v in instructions:
        if ins == 'F':
            for k in ship:
                ship[k] += waypoint[k] * v
        elif ins == 'L' or ins == 'R':
            newWaypoint = waypoint.copy()
            for f in waypoint:
                newface = getRotationResult(f,ins,v)
                newWaypoint[newface] = waypoint[f]

            waypoint = newWaypoint
        else:
            waypoint[ins] += v

    return getManhattanDist(ship)

with open('input-01.txt') as f:
    instructions = []
    for l in f.readlines():
        instructions.append([l[:1],int(l[1:])])

    print(part1(instructions),part2(instructions))