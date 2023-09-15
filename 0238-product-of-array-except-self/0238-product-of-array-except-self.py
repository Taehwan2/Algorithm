class Solution(object):
    def productExceptSelf(self, nums):
          #인덱스자리별로 자신을 제외한 왼쪽값의 합과 오른쪽 값의 합을 구하면 된다.
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
