class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        for i in range(size/2,0,-1):
            if size % i == 0:
                substr = ''
                for n in range(size/i):
                    substr+= str[:i]
                if substr == str: return True
        return False