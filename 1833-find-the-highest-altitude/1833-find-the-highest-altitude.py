class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        sum = 0
        temp = 0
        for i in gain:
            temp = temp+i
            sum = max(sum,temp)
        return sum