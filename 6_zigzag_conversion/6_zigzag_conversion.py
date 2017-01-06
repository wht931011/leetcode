class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        res=''
        size = 2*numRows - 2
        for r in range(numRows):
            j = r
            while j < len(s):
                res += s[j]
                if r != 0 and r != numRows-1:
                    if j+size-(2*r) < len(s):
                        res += s[j+size-(2*r)]
                j += size
        return res