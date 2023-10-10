class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] +=1
            else:
                dic[i]=1
        occurrence_counts = list(dic.values())
        
        return len(occurrence_counts) == len(set(occurrence_counts))
