class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, mid, high = 0, x/2,x
        while low <= high:
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid+1
            mid = (high+low) / 2
        return mid