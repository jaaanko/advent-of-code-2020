from collections import deque
from itertools import islice

def part1(p1Cards,p2Cards):
    while p1Cards and p2Cards:
        p1Top, p2Top = p1Cards.popleft(), p2Cards.popleft()

        if p1Top > p2Top:
            p1Cards.append(p1Top)
            p1Cards.append(p2Top)
        else:
            p2Cards.append(p2Top)
            p2Cards.append(p1Top)
    
    winningDeck = p1Cards or p2Cards
    i = len(winningDeck)
    res = 0

    for card in winningDeck:
        res += card * i
        i -= 1

    return res

def part2(p1Cards,p2Cards):
    seen = set()

    while p1Cards and p2Cards:
        currConfig = str(p1Cards) + ' ' + str(p2Cards)

        if currConfig in seen:
            return [1,p1Cards]

        seen.add(currConfig)

        p1Top, p2Top = p1Cards.popleft(), p2Cards.popleft()
        winner = 1 if p1Top > p2Top else 2

        if p1Top <= len(p1Cards) and p2Top <= len(p2Cards):
            winner = part2(deque(islice(p1Cards,0,p1Top)),deque(islice(p2Cards,0,p2Top)))[0]
        
        if winner == 1:
            p1Cards.append(p1Top)
            p1Cards.append(p2Top)
        else:
            p2Cards.append(p2Top)
            p2Cards.append(p1Top)
    
    return [1,p1Cards] if p1Cards else [2,p2Cards]

with open('input-01.txt') as f:
    p1,p2 = f.read().split('\n\n')
    p1Cards = deque([int(card) for card in p1.split(':\n')[1].split('\n')])
    p2Cards = deque([int(card) for card in p2.split(':\n')[1].split('\n')])

    print(part1(p1Cards.copy(),p2Cards.copy()))

    part2WinningDeck = part2(p1Cards.copy(),p2Cards.copy())[1]
    i = len(part2WinningDeck)
    part2Answer = 0

    for card in part2WinningDeck:
        part2Answer += card * i
        i -= 1
    
    print(part2Answer)