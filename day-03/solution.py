def part1(matrix,right,down):
    trees = j = 0

    for i in range(0,len(matrix),down):
        trees += matrix[i][j % len(matrix[0])] == '#'
        j += right

    return trees

with open('input-01.txt') as f:
    matrix = []

    for l in f.readlines():
        matrix.append([c for c in l.strip()])    

    print(part1(matrix,3,1))

    part2Answer = 1

    for right,down in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        part2Answer *= part1(matrix,right,down)

    print(part2Answer)