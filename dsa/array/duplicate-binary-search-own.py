import pdb


def duplicate_binary_search(nums,target):
    i,j = 0, len(nums) -1
    index = -1
    num_in_right = False
    while i<=j:
        mid = (i+j) // 2
        if nums[mid] == target:
            index = mid
            param_i = mid if num_in_right else i
            return recursive_binary_search(nums,target,index,j=mid-1,i=param_i)

        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
            num_in_right = True
    return index

def recursive_binary_search(nums,target,index,i,j):
    while i<=j:
        mid = (i+j) // 2
        if nums[mid] == target:
            index = mid
            return recursive_binary_search(nums,target,index,i=i,j=mid-1)
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return index

print(duplicate_binary_search([1,2,2,6,6,6,6,6,6,8,8],6))
print(duplicate_binary_search([2, 4, 4, 4, 10],4))
print(duplicate_binary_search([5,5,5,5,5,5,5,5,5],5))
print(duplicate_binary_search([1,2,3,4,5,6,6,6,6,6,6],6))