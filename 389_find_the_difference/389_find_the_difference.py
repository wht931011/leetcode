class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in t:
            if c not in s:
                return c
        dict_t = {}
        for c in t:
            if c not in dict_t:
                dict_t[c] = 1
            else:
                dict_t[c] += 1
        
        for c in s:
            dict_t[c] -= 1
        
        for c in dict_t:
            if dict_t[c]!=0: return c
            