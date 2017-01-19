class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        res = 0
        has_odd = False
        for c in d:
            res += d[c]
            if d[c] % 2 == 1:
                res -= 1
                has_odd = True
        if has_odd: res +=1
        return res