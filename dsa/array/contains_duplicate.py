# Input: nums = [1,2,3,1]
# Output: true


def contains_duplicate(nums):
    hashset = set()

    for i in range(len(nums)):
        if nums[i] in hashset:
            return True
        hashset.add(nums[i])
    return False

print(contains_duplicate(nums = [1,2,3,1]))