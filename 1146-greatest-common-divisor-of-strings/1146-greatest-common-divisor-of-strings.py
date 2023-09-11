class Solution(object):
    def gcdOfStrings(self,str1, str2):
    
        if str1 + str2 != str2 + str1:
            return ""

        for i in range(max(len(str1), len(str2)), 0, -1):
            print(len(str1)%i,i,len(str1))
            if len(str1) % i == 0 and len(str2) % i == 0:
                return max(str1, str2)[:i]
