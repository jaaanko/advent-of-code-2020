from collections import defaultdict

def part1(ticketFields,nearbyTickets):
    valid = set()

    for ticket in nearbyTickets:
        for fieldValue in ticket:
            for fieldRange in ticketFields.values():
                r1,r2 = fieldRange  
                if r1[0] <= fieldValue <= r1[1] or r2[0] <= fieldValue <= r2[1]:
                    valid.add(fieldValue)
                    break

    res = 0

    for ticket in nearbyTickets:
        for fieldValue in ticket:
            if fieldValue not in valid:
                res += fieldValue

    return (res,valid)

def part2(ticketFields,nearbyValidTickets,myTicket):
    answers = {}
    cannots = []

    for j in range(len(ticketFields)): 
        cannot = set()
        for i in range(len(nearbyValidTickets)):
            fieldValue = nearbyValidTickets[i][j]
            if fieldValue == -1:
                continue

            for field,fieldRange in ticketFields.items():
                r1,r2 = fieldRange  
                if (r1[0] > fieldValue or fieldValue > r1[1]) and (r2[0] > fieldValue or fieldValue > r2[1]):
                    cannot.add(field)                        
                        
        cannots.append([j,cannot])
    
    cannots.sort(key=lambda x: len(x[1]))
    answers = {}
    removed = set()

    for i in range(len(cannots)-1,-1,-1):
        for field in ticketFields:
            if field in removed:
                continue
            if field not in cannots[i][1]:
                removed.add(field)
                answers[field] = cannots[i][0]

    res = 1
    for field,value in answers.items():
        if "departure" in field:
            res *= myTicket[value]

    return res

with open('input-01.txt') as f:
    fields,myTicket,nearbyTickets = f.read().split('\n\n')
    ticketFields = defaultdict(list)

    for field in fields.split('\n'):
        fieldName,ranges = field.split(': ')

        for r in ranges.split(' or '):
            r1,r2 = map(int,r.split('-'))
            ticketFields[fieldName].append((r1,r2))
    
    nearbyTickets = [[int(n) for n in t.split(',')] for t in nearbyTickets.split(":\n")[1].split("\n")]
    numOfInvalid, valid = part1(ticketFields,nearbyTickets)
    myTicket = [int(n) for n in myTicket.split(':\n')[1].split(',')]

    for i in range(len(nearbyTickets)):
        for j in range(len(nearbyTickets[i])):
            if nearbyTickets[i][j] not in valid:
                nearbyTickets[i][j] = -1

    print(numOfInvalid,part2(ticketFields,nearbyTickets,myTicket))