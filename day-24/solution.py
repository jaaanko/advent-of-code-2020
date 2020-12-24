def flip(tiles,x,y):
    if (x,y) not in tiles or not tiles[(x,y)]:
        tiles[(x,y)] = 1
    else:
        tiles[(x,y)] = 0
    
def southWest(x,y):
    x -= y % 2 == 0
    y -= 1
    return x,y

def southEast(x,y):
    x += y % 2 == 1
    y -= 1
    return x,y

def northWest(x,y):
    x -= y % 2 == 0
    y += 1
    return x,y

def northEast(x,y):
    x += y % 2 == 1
    y += 1  
    return x,y

def east(x,y):
    x += 1
    return x,y

def west(x,y):
    x -= 1
    return x,y

def part1(directions):
    tiles = {}

    for sequence in directions:
        x = y = i = 0

        while i < len(sequence):
            if sequence[i] == "e":
                x,y = east(x,y)
            elif sequence[i] == "w":
                x,y = west(x,y)
            elif sequence[i] == "s":
                if sequence[i+1] == "e":
                    x,y = southEast(x,y)
                if sequence[i+1] == "w":
                    x,y = southWest(x,y)
            elif sequence[i] == "n":
                if sequence[i+1] == "e":
                    x,y = northEast(x,y)
                if sequence[i+1] == "w":
                    x,y = northWest(x,y)
            
            i += 1 + (sequence[i] == "n" or sequence[i] == "s")

        flip(tiles,x,y)

    return tiles

def grow(tiles):
    for x,y in list(tiles):
        for getCoords in {east,west,southEast,southWest,northEast,northWest}:
            x1,y1 = getCoords(x,y)

            if (x1,y1) not in tiles:
                tiles[(x1,y1)] = 0

def countAdjacentBlackTiles(tiles,x,y):
    res = 0

    for getCoords in {east,west,southEast,southWest,northEast,northWest}:
        x1,y1 = getCoords(x,y)
        res += (x1,y1) in tiles and tiles[(x1,y1)]

    return res

def part2(tiles,days):
    for _ in range(days):
        grow(tiles)
        new = tiles.copy()

        for x,y in list(tiles):
            adjacentBlackTiles = countAdjacentBlackTiles(tiles,x,y)

            if (tiles[(x,y)] and (not adjacentBlackTiles or adjacentBlackTiles > 2)) or (not tiles[(x,y)] and adjacentBlackTiles == 2):
                flip(new,x,y)
        
        tiles = new

    return tiles

with open('input-01.txt') as f:
    directions = []

    for tile in f.readlines():
        directions.append(tile)

    tiles = part1(directions)
    print(sum(tiles.values()),sum(part2(tiles,100).values()))