class Node:
    def __init__(self, next=None, prev=None, val=None):
        self.next = next
        self.prev = prev 
        self.val = val

class CircularDLL:
    def __init__(self, maxSize, head=None):
        self.head = head
        self.lookup = [None] * (maxSize+1)
        self.size = 0

    def append(self, val):
        newNode = Node(val=val)

        if self.head is None:
            newNode.prev = newNode.next = newNode
            self.head = newNode
        else:
            newNode.next = self.head
            last = self.head.prev
            self.head.prev = newNode
            newNode.prev = last
            last.next = newNode
        
        self.lookup[val] = newNode
        self.size += 1

    def remove(self, node):	
        if self.head.next == self.head:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.head == node:
                self.head = node.next

        self.size -= 1

    def appendAfter(self, targetNode, val):
        newNode = Node(val=val)
        self.lookup[val] = newNode
        
        newNode.prev = targetNode
        newNode.next = targetNode.next
        newNode.next.prev = newNode
        targetNode.next = newNode
        
        self.size += 1

        return newNode

    def get(self, val):
        return self.lookup[val]

def play(cups,moves):
    currCup = cups.head
    n = cups.size

    for _ in range(moves):
        pickedUp = []
        ptr = currCup.next

        for _ in range(3):
            pickedUp.append(ptr.val)
            cups.remove(ptr)
            ptr = ptr.next

        pickedUpSet = set(pickedUp)
        destVal = currCup.val - 1

        while not destVal or destVal in pickedUpSet:
            destVal -= 1

            if destVal <= 0:
                destVal = n
                
        destNode = cups.get(destVal)
        
        for p in pickedUp:
            destNode = cups.appendAfter(destNode,p)

        currCup = currCup.next

    return cups

problemInput = "158937462"
part1Cups = CircularDLL(9)

for num in problemInput:
    num = int(num)
    part1Cups.append(num)
    
play(part1Cups,100)

ptr = part1Cups.get(1).next
part1Res = []

while ptr and ptr.val != 1:
    part1Res.append(ptr.val)
    ptr = ptr.next

print(''.join(str(d) for d in part1Res))

maxCup = float('-inf')
part2Cups = CircularDLL(1000000)

for num in problemInput:
    num = int(num)
    part2Cups.append(num)
    maxCup = max(maxCup,num)

for num in range(maxCup+1,1000001):
    part2Cups.append(num)

play(part2Cups,10000000)

ptr = part2Cups.get(1)
print(ptr.next.val * ptr.next.next.val)