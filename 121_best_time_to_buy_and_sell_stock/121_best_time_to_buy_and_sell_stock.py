class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        res = 0
        min = prices[0]
        for num in prices:
            if num < min:
                min = num
            else:
                res = max(res,num-min)
        return res