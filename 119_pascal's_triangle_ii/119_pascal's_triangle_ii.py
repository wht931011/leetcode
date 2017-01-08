class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <0: return []
        res = []
        pre = 0
        # in row[rowIndex], there is rowIndex + 1 elements.
        for _ in range(rowIndex + 1):
            res.append(0)
        for i in range(rowIndex + 1):
            # set current to 1
            res[i] = 1
            # from back to start. avoid modfying the value we need
            # 10000 -> 11000 -> 11100 -> 12100 -> 12110 -> 12310 -> 13310 ->
            # 13311 -> 13341 -> 13641 -> 14641
            for j in range(i-1,0,-1):
                res[j] += res[j-1]
        return res