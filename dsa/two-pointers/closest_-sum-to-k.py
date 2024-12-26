def closest_sum_to_k(nums,target):
    difference = float("inf")
    res = []
    i,j = 0,len(nums) - 1

    while i<j:
        cur_sum = nums[i] + nums[j]
        cur_sum_diff = abs(target - cur_sum)
        if cur_sum_diff <= difference:
            res = [nums[i], nums[j]] 
            difference = cur_sum_diff
        
        if cur_sum < target:
            i+=1
        else:
            j-=1
    return res

print(closest_sum_to_k([1, 3, 4, 7, 10],15))