class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                n = i
                for m in range(i+1,len(nums)):
                    if nums[m] != 0:
                        nums[n] = nums[m]
                        nums[m] = 0
                        n += 1