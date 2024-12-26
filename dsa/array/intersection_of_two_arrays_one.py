# nums1 = [1,2,2,1], nums2 = [2,2]
# output = [2]

# nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# output = [9,4]  / [4,9]


def intersection_of_two_arrays_one(nums1,nums2):
    nums_1 = list(set(nums1))  
    nums_2 = set(nums2)

    res = []

    for i in range(len(nums_1)):
        if nums_1[i] in nums_2:
            res.append(nums_1[i])
    return res

print(intersection_of_two_arrays_one(nums1=[1,2,2,1],nums2=[2,2]))
print(intersection_of_two_arrays_one(nums1=[9,4],nums2=[9,4,9,8,4]))
            

