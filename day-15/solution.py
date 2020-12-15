def part1(nums,n):
    spoken = [None] * (n+1) # Use list instead of a dictionary to speed up part 2

    for i in range(len(nums)):
        spoken[nums[i]] = (i+1,i+1)

    prev = nums[-1]

    for turn in range(len(nums)+1,n+1):
        prev = spoken[prev][1] - spoken[prev][0]

        if not spoken[prev]:
            spoken[prev] = (turn,turn)
        else:
            spoken[prev] = (spoken[prev][1],turn)

    return prev

nums = [2,15,0,9,1,20]
print(part1(nums,2020),part1(nums,30000000))