def getAdjacent4d(x,y,z,w):
    adjacent = []

    for x1 in range(x-1,x+2):
        for y1 in range(y-1,y+2):
            for z1 in range(z-1,z+2):
                for w1 in range(w-1,w+2):
                    if x1 == x and y1 == y and z1 == z and w1 == w:
                        continue
                    adjacent.append((x1,y1,z1,w1))

    return adjacent 

def getAdjacent3d(x,y,z):
    adjacent = []

    for x1 in range(x-1,x+2):
        for y1 in range(y-1,y+2):
            for z1 in range(z-1,z+2):
                if x1 == x and y1 == y and z1 == z:
                    continue
                adjacent.append((x1,y1,z1))

    return adjacent 

def part1(pocket,cycles):
    for cycle in range(cycles):
        toUpdate = []

        for x,y,z in list(pocket):
            for adj in getAdjacent3d(x,y,z):
                x1,y1,z1 = adj
                if (x1,y1,z1) not in pocket:
                    pocket[(x1,y1,z1)] = "."

        for x,y,z in list(pocket):
            numActive = 0
            for adj in getAdjacent3d(x,y,z):
                x1,y1,z1 = adj
                if (x1,y1,z1) not in pocket:
                    pocket[(x1,y1,z1)] = "."

                if pocket[(x1,y1,z1)] == "#":
                    numActive += 1

            if pocket[(x,y,z)] == "#":
                if numActive != 2 and numActive != 3:
                    toUpdate.append((x,y,z))
            elif numActive == 3:
                toUpdate.append((x,y,z))
        
        for x,y,z in toUpdate:
            pocket[(x,y,z)] = '#' if pocket[(x,y,z)] == "." else "."
        
        print("Finished Cycle",cycle)

    res = 0
    for v in pocket.values():
        res += v == "#"
    
    return res

def part2(pocket,cycles):
    for cycle in range(cycles):
        toUpdate = []

        for x,y,z,w in list(pocket):
            for adj in getAdjacent4d(x,y,z,w):
                x1,y1,z1,w1 = adj
                if (x1,y1,z1,w1) not in pocket:
                    pocket[(x1,y1,z1,w1)] = "."

        for x,y,z,w in list(pocket):
            numActive = 0
            for adj in getAdjacent4d(x,y,z,w):
                x1,y1,z1,w1 = adj
                if (x1,y1,z1,w1) not in pocket:
                    pocket[(x1,y1,z1,w1)] = "."

                if pocket[(x1,y1,z1,w1)] == "#":
                    numActive += 1

            if pocket[(x,y,z,w)] == "#":
                if numActive != 2 and numActive != 3:
                    toUpdate.append((x,y,z,w))
            elif numActive == 3:
                toUpdate.append((x,y,z,w))
        
        for x,y,z,w in toUpdate:
            pocket[(x,y,z,w)] = '#' if pocket[(x,y,z,w)] == "." else "."
        
        print("Finished Cycle",cycle)

    res = 0
    for v in pocket.values():
        res += v == "#"
    
    return res

# Possible improvement: generalize solution to N dimensions
with open('input-01.txt') as f:
    pocket3d = {}
    pocket4d = {}
    grid = f.read().split('\n')

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pocket3d[(i,j,0)] = grid[i][j]
            pocket4d[(i,j,0,0)] = grid[i][j]

    print(part1(pocket3d,6))
    print(part2(pocket4d,6))