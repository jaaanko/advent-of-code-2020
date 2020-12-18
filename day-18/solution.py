def solvePart1(expression): # Solves an expression w/o parentheses, following the rules in part 1 
    expression = expression.split(' ')
    prev = int(expression[0])

    for i in range(1,len(expression)-1,2):
        if expression[i] == "+":
            prev += int(expression[i+1])
        elif expression[i] == "*":
            prev *= int(expression[i+1])

    return prev

def solvePart2(expression): # Solves an expression w/o parentheses, following the rules in part 2
    expression = expression.split(' ')
    stack = [int(expression[0])]

    for i in range(2,len(expression)):
        if expression[i-1] == "+":
            stack.append(stack.pop() + int(expression[i]))
        elif expression[i].isdigit():
            stack.append(int(expression[i]))

    res = 1
    for n in stack:
        res *= n

    return res

def part1(expressions,solve):
    res = 0

    for expression in expressions:
        stack = []

        # Evaluate all expressions inside parentheses until we are left with a simple expression w/o parentheses
        for i in range(len(expression)):
            if expression[i] == '':
                continue
            if expression[i] == ")":
                inside = []        

                while stack and stack[-1] != "(":
                    inside.append(stack.pop())
                
                if stack: 
                    stack.pop()
                
                stack.append(str(solve(' '.join(inside[::-1]))))
            else:
                stack.append(expression[i])

        # Once we have evaluated all expressions inside parentheses, pass the final expression into our solve function
        # to get the answer
        res += solve(' '.join(stack))

    return res

with open('input-01.txt') as f:
    expressions = [expression.rstrip().replace('(',' ( ').replace(')',' ) ').split(' ') for expression in f.readlines()]
    print(part1(expressions,solvePart1),part1(expressions,solvePart2))