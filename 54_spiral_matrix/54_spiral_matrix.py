class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []
        s1 = 0
        f1 = 0
        f2 = len(matrix)
        e1 = len(matrix[0])
        res = []
        size = len(matrix) * len(matrix[0])
        while len(res) != size:
            for n in range(s1,e1):
                if len(res) == size: break
                res.append(matrix[f1][n])
            for n in range(f1+1,f2):
                if len(res) == size: break
                res.append(matrix[n][e1-1])
            for n in range(e1-1-1,s1-1,-1):
                if len(res) == size: break
                res.append(matrix[f2-1][n])
            for n in range(f2-1-1,f1,-1):
                if len(res) == size: break
                res.append(matrix[n][s1])
            s1 +=1
            f1 +=1
            f2 -=1
            e1 -=1
        return res