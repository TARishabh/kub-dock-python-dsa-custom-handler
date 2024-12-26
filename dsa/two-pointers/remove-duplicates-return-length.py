def remove_duplicates(nums):
    length = 0

    for i in range(len(nums)):
        if nums[i] != nums[i-1]:
            length+=1
    return length

print(remove_duplicates([1, 1, 2]))  # Expected output: 2



# # def remove_duplicates_return_length(nums):
# #     length = 0
# #     i,j = 0,len(nums) - 1
# #     prev_i, prev_j = float("inf")

# #     while i < j:
# #         if nums[i] != nums[prev_i] and nums[j] != nums[prev_j]:
# #             length+=2

# #         elif nums[i] == nums[prev_i] and nums[j] != nums[prev_j]:
# #             length +=1
        
# #         elif nums[i] != nums[prev_i] and nums[j] == nums[prev_j]:
# #             length +=1
        
# #         prev_i,prev_j = i,j
# #         i+=1
# #         j-=1

# #     return length

# # print(remove_duplicates_return_length([1,1,2]))


# def remove_duplicates_return_length(nums):
#     length = 0
#     i, j = 0, len(nums) - 1
#     prev_i, prev_j = -1, -1  # Initialize with -1 to skip first comparison

#     while i <= j:
#         # Handle the first element and unique increments
#         if prev_i >= 0 and nums[i] != nums[prev_i]:
#             length += 1
#         elif prev_i == -1:
#             length += 1  # First element

#         if prev_j >= 0 and nums[j] != nums[prev_j] and i != j:
#             length += 1
#         elif prev_j == -1 and i != j:
#             length += 1  # First element from the right side, if i != j
        
#         prev_i, prev_j = i, j
#         i += 1
#         j -= 1

#     return length

# # Test case
# print(remove_duplicates_return_length([1, 1, 2]))  # Expected output: 2
