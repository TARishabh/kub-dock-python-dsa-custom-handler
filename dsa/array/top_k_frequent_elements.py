# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


def top_k_freq_elements(nums,k):
    hashmap = {}

    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

    res = []
    for num,cnt in hashmap.items():
        res.append([cnt,num])
    
    res.sort()
    
    arr = []
    for i in range(k):
        arr.append(res.pop()[1])
    
    return arr

print(top_k_freq_elements(nums = [1,1,1,2,2,3], k = 2))

            

