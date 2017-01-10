class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res= []
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res