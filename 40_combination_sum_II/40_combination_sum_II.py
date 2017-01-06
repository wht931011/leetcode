class Solution(object):
    def helper(self, res, candidates, target, index, sub_res):
        if target == 0:
            if sub_res not in res:
                res.append(sub_res)
            return 
        else:
            for i in range(index,len(candidates)):
                if target< candidates[i]:
                    return
                self.helper(res, candidates, target-candidates[i],i+1,sub_res + [candidates[i]])
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        sub_res = []
        self.helper(res,candidates,target,0,sub_res)
        return res