class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row,col,cube = [],[],[]
        for i in range(9):
            row.append([])
            col.append([])
            cube.append([])
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    c = i/3*3 + j/3
                    cube[c].append(board[i][j])
        for i in range(9):
            if len(row[i]) != len(set(row[i])) or len(col[i]) != len(set(col[i])) or len(cube[i]) != len(set(cube[i])):
                return False
        
        return True