"""
Given an array, move all zeros to the end while maintaining the order of the other elements.
Example: [0,1,0,3,12] should become [1,3,12,0,0]. Explain the time and space complexity.
"""

"""
Time Complexity -> O(n)
Space Complexity -> O(1)
"""

def move_all_zeros(nums):
    i, j = 0,1

    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
        elif nums[i] == 0 and nums[j] == 0:
            j+=1
            continue
        i+=1
        j+= 1

    return nums

nums = [[0,1,0,3,12], [1,0,3,0,12], [1,3,12,0,0], [0,0,1,3,12]]

for i in nums:
    print(move_all_zeros(i))




"""
Strict Code
"""

def move_all_zeros(nums):
    i, j = 0,1

    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j+= 1
        elif nums[i] != 0 and nums[j] == 0:
            i+=1
            j +=1
        elif nums[i] == 0 and nums[j] == 0:
            j+=1
        elif nums[i] != 0 and nums[j] != 0:
            i+=1
            j+=1
    return nums

nums = [[0,1,0,3,12], [1,0,3,0,12], [1,3,12,0,0], [0,0,1,3,12]]

for i in nums:
    print(move_all_zeros(i))



