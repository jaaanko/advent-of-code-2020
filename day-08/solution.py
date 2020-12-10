def part1(instructions):
    accumulator = 0

    seen = set()
    i = 0

    while i < len(instructions):
        if i in seen:
            return (accumulator,True)

        seen.add(i)
        command, value = instructions[i].split(' ')
        value = int(value)

        if command == "jmp":
            i += value
        elif command == "acc":
            accumulator += value

        i += command != "jmp"
    
    return (accumulator,False)

def part2(instructions):
    for i in range(len(instructions)):
        command,value = instructions[i].split(' ')
        oldCommand = command 

        if oldCommand == "jmp":
            instructions[i] = "nop " + value
        elif oldCommand == "nop":
            instructions[i] = "jmp " + value

        accumulator, infiniteLoop = part1(instructions)

        if not infiniteLoop:
            return accumulator
        
        instructions[i] = oldCommand + " " + value

    return -1

with open('input-01.txt') as f:
    instructions = f.read().strip().split('\n')
    print(part1(instructions)[0],part2(instructions))