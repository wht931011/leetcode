class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        res = 0
        i = 0
        for n in range(len(s)):
            if i == len(g):
                break
            if s[n] >= g[i]:
                res += 1
                i+=1
        return res