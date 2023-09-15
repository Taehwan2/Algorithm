class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        temp = 1 
        for i in range(len(nums)): 
            output.append(temp) 
            temp *= nums[i] 
        temp = 1
        for i in range(len(nums) - 1, -1, -1):  
            output[i] *= temp  
            temp *= nums[i] 
    
        return output