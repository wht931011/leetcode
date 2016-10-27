class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2: return 0
        # deal with array with 2 el. like [2,3]
        if len(nums) == 2: 
            return 0 if nums[0]>nums[1] else 1
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        # deal with last 2 el. like [1,2,3,4]
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1 
        return 0