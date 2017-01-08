class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = []
        for i in range(numRows):
            row = [1]
            for j in range(1,i):
                preRow = res[i-1]
                row.append(preRow[j-1]+preRow[j])
            if i > 0:
                row.append(1)
            res.append(row)
        return res
                