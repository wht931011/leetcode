class Solution(object):
    def helper(self,allres,res,index,nums):
        if index == len(nums):
            if res not in allres:
                allres.append(res)
            return
        if res not in allres:
            allres.append(res)
        for i in range(index,len(nums)):
            self.helper(allres,res+[nums[i]],i+1,nums)
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        allres = []
        self.helper(allres,[],0,nums)
        return allres
    
        