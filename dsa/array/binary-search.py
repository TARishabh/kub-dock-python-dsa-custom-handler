def binary_search(nums,target):
    i, j = 0,len(nums) - 1

    while i<=j:
        mid = (i+j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1

print(binary_search([2, 4, 4, 4, 10],10))
