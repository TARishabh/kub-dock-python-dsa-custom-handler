nums,target = [2,7,11,15], 9
nums,target = [3,2,4], 6


def two_sum(nums,target):
    hashmap = {}

    for i in range(len(nums)):
        if target - nums[i]  in hashmap:
            return [hashmap[target-nums[i]],i]
        hashmap[nums[i]] = i

print(two_sum(nums,target))
