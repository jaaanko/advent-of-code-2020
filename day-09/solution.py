def part1(nums,preamble):
    for i in range(preamble,len(nums)):
        if twoSum(nums[i-preamble:i],nums[i]) == -1:
            return nums[i]

    return -1

def part2(nums,target):
    currSum = nums[0]
    j = 0

    for i in range(1,len(nums)):
        currSum += nums[i]

        while currSum > target:
            currSum -= nums[j]
            j += 1
        
        if currSum == target:
            numsSlice = nums[j:i+1]
            return min(numsSlice) + max(numsSlice)

    return -1
    
def twoSum(nums,target):
    s = set()

    for n in nums:
        if n in s:
            return n*(target-n)

        s.add(target-n)
    
    return -1

with open('input-01.txt') as f:
    nums = [int(n) for n in f.readlines()]
    part1Answer = part1(nums,25)
    print(part1Answer,part2(nums,part1Answer))