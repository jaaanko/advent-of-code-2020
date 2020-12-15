import math, itertools
from collections import defaultdict

def binaryToDecimal(bitlist):
    out = 0

    for bit in bitlist:
        out = (out << 1) | bit

    return out

def decimalToBinary(num):
    bits = int(max(36, math.log(num, 2)+1))
    return [1 if num & (1 << (bits-1-n)) else 0 for n in range(bits)]

def applyMaskPart1(mask,bits):
    bits = bits[:]

    for i in range(len(bits)):
        if mask[i] != 'X':
            bits[i] = int(mask[i])
    
    return bits

def part1(maskToInstructions):
    mem = {}
    res = 0

    for mask,instructions in maskToInstructions.items():
        for address,value in instructions:
            mem[address] = binaryToDecimal(
                applyMaskPart1(
                    mask,
                    decimalToBinary(value)
                )
            )

    for value in mem.values():
        if value:
            res += value

    return res

def applyMaskPart2(mask,bits):
    bits = bits[:]

    for i in range(len(bits)):
        if mask[i] != '0':
            bits[i] = mask[i]

    return bits

def part2(maskToInstructions):
    mem = {}
    res = 0

    for mask,instructions in maskToInstructions.items():
        numOfX = 0
        for c in mask:
            numOfX += c == 'X'

        seqs = ["".join(seq) for seq in itertools.product("01", repeat=numOfX)]

        for address,value in instructions:
            binaryAddress = applyMaskPart2(mask,decimalToBinary(address))
            
            for s in seqs:
                binaryAddressCopy = binaryAddress[:]
                j = 0

                for i in range(len(binaryAddressCopy)):
                    if binaryAddressCopy[i] == 'X':
                        binaryAddressCopy[i] = s[j]
                        j += 1
                
                mem[binaryToDecimal([int(c) for c in binaryAddressCopy])] = value

    for value in mem.values():
        if value:
            res += value

    return res

with open("input-01.txt") as f:
    mask = ""    
    maskToInstructions = defaultdict(list)

    for l in f.readlines():
        if l[:4] == "mask":
            mask = l.split(' = ')[1].rstrip()            
        else:
            ins,value = l.split(' = ')
            value = int(value)
            address = int(ins[4:len(ins)-1])
            maskToInstructions[mask].append((address,value))
    
    print(part1(maskToInstructions),part2(maskToInstructions))