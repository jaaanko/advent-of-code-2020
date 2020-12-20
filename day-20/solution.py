class Tile:
    def __init__(self,tileId,left,right,top,bottom):
        self.tileId = tileId
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

def numOfSameBorders(tileId,borders):
    count = 0

    for k,v in borders.items():
        if k == tileId:
            continue
        count += len(borders[tileId].intersection(v))   

    return count

def part1(tiles):
    borders = {}

    for tileId, tile in tiles.items():
        n = len(tile)
        m = len(tile[0])

        left = ''.join([tile[i][0] for i in range(n)])
        right = ''.join([tile[i][m-1] for i in range(n)])
        top = ''.join([tile[0][j] for j in range(m)])
        bottom = ''.join([tile[n-1][j] for j in range(m)])

        borders[tileId]= set([left,right,top,bottom] + [left[::-1],right[::-1],top[::-1],bottom[::-1]])

    res = 1

    for tileId in borders:
        if numOfSameBorders(tileId,borders) == 4:
            res *= int(tileId)

    return res

with open('input-01.txt') as f:
    tiles = {}
    
    for tile in f.read().split('\n\n'):
        tileId, grid = tile.split(':\n')
        tileId = tileId.split(' ')[1]
        tiles[tileId] = [line for line in grid.split('\n')]
    
    print(part1(tiles))