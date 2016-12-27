class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 1
        INT_MAX = 2147483647
        result,sum,count = 0,0,0
        isP = True if (dividend > 0 and divisor > 0) or (dividend<0 and divisor < 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            sum = divisor
            count = 1
            while sum + sum <= dividend:
                sum += sum
                count += count
            dividend -= sum
            result += count
        return min(result,INT_MAX) if isP else 0-result