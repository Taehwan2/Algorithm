class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        
     
        while index < len(nums):
            nums[index] = 0
            index += 1
        
        return nums