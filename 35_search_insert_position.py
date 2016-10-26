class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<1: return 0
        if len(nums)==1: return 0 if nums[0]>=target else 1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)