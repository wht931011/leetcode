class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = False
        re = [-1,-1]
        if len(nums) == 0: return [-1,-1]
        for i in range(len(nums)):
            if found==False and nums[i] == target:
                    found = True
                    re[0] = i
            if found==True and nums[i] == target:
                    re[1] = i
        return re
                    