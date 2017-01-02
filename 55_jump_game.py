class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i in range(len(nums)):
            if i > max_jump or max_jump >= len(nums)-1:
                break
            max_jump = max(max_jump,i+nums[i])
        return True if max_jump>=len(nums)-1 else False