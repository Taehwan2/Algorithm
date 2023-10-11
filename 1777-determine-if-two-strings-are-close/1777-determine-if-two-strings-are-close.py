class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dic1= {}
        dic2 = {}
        for i in word1:
            if i in dic1:
                dic1[i] +=1
            else:
                dic1[i] = 1
        for i in word2:
            if i in dic2:
                dic2[i] +=1
            else:
                dic2[i] = 1

        set1 = sorted(dic1.values())
        set2 = sorted(dic2.values())

        return set1==set2 and sorted(dic1.keys()) == sorted(dic2.keys())