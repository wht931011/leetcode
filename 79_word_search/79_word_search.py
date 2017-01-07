class Solution(object):
    def search(self,board,word,m,n):
        if len(word) == 0:
            return True
        if m >= len(board) or n >= len(board[0]) or m<0 or n<0 or board[m][n] != word[0]:
            return False
        board[m][n] = '#'
        if self.search(board,word[1:],m+1,n) or self.search(board,word[1:],m,n+1) or self.search(board,word[1:],m-1,n) or self.search(board,word[1:],m,n-1):
            return True
        board[m][n] = word[0]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board)<1 or len(board[0])<1 or word == '':
            return False
        for m in range(len(board)):
            for n in range(len(board[0])):
                if self.search(board,word,m,n):
                    return True
        return False