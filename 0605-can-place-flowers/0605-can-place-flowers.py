class Solution(object):
    def canPlaceFlowers(self,candies, extraCandies):

        count = len(candies)
        for i in range(0,count):
            left,right= i-1 , i+1
            if(candies[i]==0 and (left<0 or candies[left]==0) and (right==count or candies
            [right]==0)):
                candies[i]=1
                extraCandies-=1

        if(extraCandies>0):
                return False

        return True
        