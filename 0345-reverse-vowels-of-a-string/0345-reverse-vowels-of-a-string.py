class Solution(object):
    def reverseVowels(self, s):
        strarr = "aeiouAEIOU" 
        s_list = list(s)  
        a, b = 0, len(s) - 1 
        while a < b:
            if s_list[a] in strarr and s_list[b] in strarr:
                s_list[a], s_list[b] = s_list[b], s_list[a]
                a += 1
                b -= 1
            elif s_list[a] not in strarr:
                a += 1
            elif s_list[b] not in strarr:
                b -= 1
        return "".join(s_list)  

        