class Solution(object):
    def helper(self,n,allres,res,left,right):
        if left < right:
            return 
        if left == n and right == n :
            allres.append(res)
            return 
        if(left<n):
            self.helper(n,allres,res+'(',left+1,right)
        if(right<n):
            self.helper(n,allres,res+')',left,right+1)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        allres = []
        res = ''
        self.helper(n,allres,res,0,0)
        return allres