class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = [],[]
        for i in range(len(matrix)):
            for m in range(len(matrix[0])):
                if matrix[i][m] == 0:
                    row.append(i)
                    col.append(m)
                    
        for i in row:
            for y in range(len(matrix[0])):
                matrix[i][y] = 0
        for m in col:
            for x in range(len(matrix)):
                matrix[x][m] = 0