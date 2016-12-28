class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        res = ''
        for i in range(len(s)):
            if s[i] in dict:
                res += dict[s[i]]
            else:
                res += t[i]
                if t[i] in dict.values(): return False
                dict[s[i]] = t[i]
        return True if res == t else False