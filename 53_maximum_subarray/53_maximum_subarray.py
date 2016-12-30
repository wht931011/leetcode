class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        s = 0
        for n in nums:
            if s < 0:
                s = n
            else:
                s += n
            m = max(s,m)
        return m