def getLoopSizes(cardPublicKey,doorPublicKey):
    doorLoopSize = cardLoopSize = val = 1
    subjectNum = 7
    doorLoopSizeFound = cardLoopSizeFound = False

    while not cardLoopSizeFound or not doorLoopSizeFound:
        val = (val * subjectNum) % 20201227

        if val == doorPublicKey:
            doorLoopSizeFound = True
        if val == cardPublicKey:
            cardLoopSizeFound = True

        doorLoopSize += not doorLoopSizeFound
        cardLoopSize += not cardLoopSizeFound
    
    return (cardLoopSize,doorLoopSize)

def part1(loopSize,publicKey):
    val = 1
    for _ in range(loopSize):
        val = (val * publicKey) % 20201227
    
    return val

card = 18356117
door = 5909654
cardLoopSize, doorLoopSize = getLoopSizes(cardPublicKey=card,doorPublicKey=door)
print(part1(doorLoopSize,card))