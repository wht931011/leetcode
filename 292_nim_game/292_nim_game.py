class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1~3 stones: win
        # 4 stones: lose
        # 5~7 stones: win
        # 8 stones: lose
        # ...
        return n % 4 != 0