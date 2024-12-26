def find_smallest_greater_or_equal(nums,target):
    i,j = 0,len(nums) -1
    index = -1

    while i<=j:
        mid = (i+j)//2

        if nums[mid] >= target:
            index = mid
            j = mid - 1
        else:
            i = mid + 1
    return index

# Test cases
print(find_smallest_greater_or_equal([2, 4, 6, 8, 10], 5))  # Output: 2 (index of 6)
print(find_smallest_greater_or_equal([1, 3, 5, 7, 9], 6))  # Output: 3 (index of 7)
print(find_smallest_greater_or_equal([1, 2, 3, 4, 5], 0))  # Output: 0 (index of 1)
print(find_smallest_greater_or_equal([2, 4, 6, 8], 10))  # Output: -1 (no number >= 10)