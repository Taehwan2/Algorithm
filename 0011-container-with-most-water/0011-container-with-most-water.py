class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        lf,rf = 0,len(height)-1
        while(lf<rf):
            temp_height = min(height[lf],height[rf])
            temp = (rf-lf) * temp_height
            print(temp)
            if(max_val<temp):
                max_val = temp
            temp = 0
            if(temp_height == height[lf]):
                lf+=1
            else:
                rf-=1
        return max_val

            