# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]


# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


def intersection_of_two_arrays_two(nums1,nums2):
    hashmap_nums_1,hashmap_nums_2 = {},{}

    for i in range(len(nums1)):
        hashmap_nums_1[nums1[i]] = hashmap_nums_1.get(nums1[i],0) + 1
    
    for i in range(len(nums2)):
        hashmap_nums_2[nums2[i]] = hashmap_nums_2.get(nums2[i],0) + 1

    res = []

    for key,val in hashmap_nums_1.items():
        if hashmap_nums_2.get(key):
            if hashmap_nums_2[key] == hashmap_nums_1[key]:
                for i in range(hashmap_nums_1[key]):
                    res.append(key)
            else:
                if hashmap_nums_1[key] > hashmap_nums_2[key]:
                    for i in range(hashmap_nums_2[key]):
                        res.append(key)
                else:
                    for i in range(hashmap_nums_1[key]):
                        res.append(key)

    return res

print(intersection_of_two_arrays_two(nums1=[1,2,2,1], nums2=[2,2]))
print(intersection_of_two_arrays_two(nums1=[4,9,5], nums2=[9,4,9,8,4]))
