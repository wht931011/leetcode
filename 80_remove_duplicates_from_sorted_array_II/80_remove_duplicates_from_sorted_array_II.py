class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return len(nums)
        size = 1
        for i in range(2,len(nums)):
            if nums[i]!= nums[size-1]:
                size += 1
                nums[size] = nums[i]
        return size + 1