def sum_of_two_num(nums,target):
    nums.sort()

    i,j = 0,len(nums) -1

    while i<j:
        cur_sum = nums[i] + nums[j]

        if cur_sum == target:
            return [i,j]
        elif cur_sum > target:
            j -= 1
        else:
            i+=1
    
    return -1

print(sum_of_two_num([1,2,4,5,6,7],9))