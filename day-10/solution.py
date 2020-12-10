from collections import defaultdict

def part1(nums):
    dif = defaultdict(int)
    for i in range(len(nums)-1):
        k = nums[i+1] - nums[i]
        dif[k] += 1

    return dif

def part2(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1

    for i in range(1,len(dp)):
        if i-1 >= 0 and nums[i] - nums[i-1] <= 3:
            dp[i] += dp[i-1]
        
        if i-2 >= 0 and nums[i] - nums[i-2] <= 3:
            dp[i] += dp[i-2]

        if i-3 >= 0 and nums[i] - nums[i-3] <= 3:
            dp[i] += dp[i-3]

    return dp[-1]

with open('input-01.txt') as f:
    nums = [int(n) for n in f.readlines()]
    nums.append(0)
    nums.sort()
    nums.append(nums[-1] + 3)

    dif = part1(nums)
    print(dif[1] * dif[3],part2(nums))