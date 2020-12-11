from collections import deque

def part1(matrix,getNextState):
    res = 0
    n = len(matrix)
    m = len(matrix[0])
    q = deque()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "L":
                q.append([i,j,"L"])
    
    leftForCurrRound = len(q)
    toUpdate = []

    while q:
        i,j,_ = q.popleft()
        leftForCurrRound -= 1
        nextState = getNextState(i,j,matrix)

        if nextState != matrix[i][j]:
            future = [i,j,nextState]
            q.append(future)
            toUpdate.append(future)
        
        if not leftForCurrRound:
            leftForCurrRound = len(q)
            for nextI,nextJ,nextState in toUpdate:
                matrix[nextI][nextJ] = nextState
            
            toUpdate = []
    
    for i in range(n):
        for j in range(m):
            res += matrix[i][j] == "#"

    return res

def getNextStatePart1(i,j,matrix):
    numOccupied = 0

    for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nextI = i + dy
        nextJ = j + dx

        if not isValid(nextI,nextJ,matrix):
            continue
        
        numOccupied += matrix[nextI][nextJ] == "#"

    if matrix[i][j] == "L" and not numOccupied:
        return '#'
    
    if matrix[i][j] == "#" and numOccupied >= 4:
        return 'L'
    
    return matrix[i][j]

def getNextStatePart2(i,j,matrix):
    numOccupied = 0

    for dy,dx in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        nextI = i + dy
        nextJ = j + dx

        if not isValid(nextI,nextJ,matrix):
            continue
        
        while isValid(nextI,nextJ,matrix) and matrix[nextI][nextJ] == ".":
            nextI += dy
            nextJ += dx

        if isValid(nextI,nextJ,matrix):
            numOccupied += matrix[nextI][nextJ] == '#'

    if matrix[i][j] == "L" and not numOccupied:
        return '#'
    
    if matrix[i][j] == "#" and numOccupied >= 5:
        return 'L'
    
    return matrix[i][j]

def isValid(i,j,matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])

with open('input-01.txt') as f:
    matrix = []

    for l in f.readlines():
        matrix.append([c for c in l.strip()])    

    print(part1([row[:] for row in matrix],getNextStatePart1),part1([row[:] for row in matrix],getNextStatePart2))