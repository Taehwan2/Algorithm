class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_arr = [0] * (len(nums) + 1)
        temp_arr[0] = 0
        index = -1
        for i in range(len(nums)):
            temp_arr[i+1] = temp_arr[i]+nums[i]
        print(temp_arr)

        last = temp_arr[len(nums)]
        for i in range(len(temp_arr)-2):
            if(temp_arr[i]==last-temp_arr[i+1]):
                index = i
                return index
        if(index==-1 and 0==temp_arr[len(temp_arr)-2]):
            index=len(temp_arr)-2

        return index