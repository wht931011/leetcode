class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # http://www.cnblogs.com/grandyang/p/6053827.html
        minimum = nums[0]
        res = 0
        for n in nums: minimum = min(minimum,n)
        for n in nums: res += (n - minimum)
        return res