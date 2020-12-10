def part1(nums,target):
    s = set()

    for n in nums:
        if n in s:
            return n*(target-n)

        s.add(target-n)
    
    return -1

def part2(nums,target):
    nums.sort()

    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1

        first = nums[i]

        while j < k:
            second = nums[j]
            third = nums[k]

            total = first + second + third

            if total == target:
                return first * second * third
            elif total < target:
                j += 1
            else:
                k -= 1
    
    return -1

with open('input-01.txt') as f:
    target = 2020
    nums = [int(l) for l in f.readlines()]
    print(part1(nums,target),part2(nums,target))