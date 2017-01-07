class Solution(object):
    def helper(self,allres,res,index,nums):
        if index == len(nums):
            allres.append(res)
            return
        allres.append(res)
        for i in range(index,len(nums)):
            self.helper(allres,res+[nums[i]],i+1,nums)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allres = []
        self.helper(allres,[],0,nums)
        return allres