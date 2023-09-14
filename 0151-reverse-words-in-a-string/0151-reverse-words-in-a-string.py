class Solution(object):
    def reverseWords(self,s):
        strarr = s.strip().split(' ')
        strarr = [word for word in strarr if word != '']
        strarr.reverse()
        return ' '.join(strarr)
        