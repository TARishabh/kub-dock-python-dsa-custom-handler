"""
Modify the above function to search for the first occurrence of a given number in a sorted array 
where duplicates are allowed (e.g., [2, 4, 4, 4, 10], target 4 should return index 1).
"""


def duplicate_binary_search(nums,target):
    i,j = 0,len(nums)-1
    index = -1

    while i<=j:
        mid = (i+j) // 2
        if nums[mid] == target:
            index = mid
            j = mid - 1
        elif nums[mid] > target:
            j = mid -1
        else:
            i = mid + 1
    return index

print(duplicate_binary_search([1,2,2,6,6,6,6,6,6,8,8],6))
print(duplicate_binary_search([2, 4, 4, 4, 10],4))
print(duplicate_binary_search([5,5,5,5,5,5,5,5,5],5))
print(duplicate_binary_search([1,2,3,4,5,6,6,6,6,6,6],6))