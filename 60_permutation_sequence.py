import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [ x+1 for x in range(n)]
        res = ''
        k-=1
        while len(res) < n:
            loop = math.factorial(len(nums)-1)
            nth_num = k / loop
            k = k % loop
            res += str(nums[nth_num])
            nums.remove(nums[nth_num])
        return res