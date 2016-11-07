class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while(True):
            dict[n] = 1
            n = sum([int(x)*int(x) for x in str(n)])
            if n == 1 or n in dict:
                break
        return n == 1