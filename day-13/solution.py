# CRT implementation from: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce

def chineseRemainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mulInv(p, n_i) * p
    return sum % prod
 
def mulInv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def getNextEarliestTime(departTime,bus):
    return departTime-(departTime%bus)+bus

def part1(departTime,buses):
    earliest = float('inf')
    earliestBus = -1

    for bus in buses:
        nextEarliest = getNextEarliestTime(departTime,bus)
        if nextEarliest < earliest:
            earliest = nextEarliest
            earliestBus = bus

    return (earliest - departTime) * earliestBus

with open('input-01.txt') as f:
    departTime, buses = f.readlines()
    availBuses = []
    remaindersNeeded = []

    for i,b in enumerate(buses.split(',')):
        if b != 'x':
            b = int(b)
            availBuses.append(b) 
            remaindersNeeded.append(b-i)
    
    print(part1(int(departTime),availBuses),chineseRemainder(availBuses,remaindersNeeded))

    '''
    Intuition for using CRT:

    Given: 7,13,x,x,59,x,31,19
    We are trying to find a time t which satisfies the following:

    t % 7 == 0 
    t % 13 == 12 (we want bus 13 to depart at t+1) 
    t % 59 == 55 (we want bus 59 to depart at t+4) 
    .
    .
    etc.

    '''