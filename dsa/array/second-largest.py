"""
find the second largest element in an array and explain its time and space complexity.
"""

"""
Time Complexity - O(n)
Space Complexity - O(1)
"""

def second_largest(nums):
    largest = float("-inf")
    second_largest = float("-inf")

    for i in nums:
        if i > largest:
            largest,second_largest = i,largest
        elif i < largest and i > second_largest:
            second_largest = i

    return second_largest

print(second_largest([1,2,3,4,5,6,50,49]))

