class Solution:
    def productExceptSelf(self, nums):
        """
        So the idea is to multiply all the elements of the array and 
        then divide each element by the current element.

        And to handle zeros, we count the number of zeros and if there are more than 1 zeros,
        we return an array of zeros. If there is only one zero, we return an 
        array with the product
        """
        product = 1
        zero_count = 0
        zero_index = -1

        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_count += 1
                zero_index = i
        
        for i in range(len(nums)):
            if zero_count >=2:
                return [0] * len(nums)
            elif zero_count == 1:
                res = [0] * len(nums)
                res[zero_index] = product
                return res
            else:
                nums[i] = product // nums[i]
        
        return nums