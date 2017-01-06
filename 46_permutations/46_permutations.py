class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[nums[0]]]
        c = 1
        for n in range(1,len(nums)):
            tmp_result = []
            for r in result:
                for i in range(c+1):
                    tmp = r[:]
                    tmp.insert(i,nums[n])
                    tmp_result.append(tmp)
            c+=1
            result = tmp_result
        return result