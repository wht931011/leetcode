class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        digit2 = 1
        for i in range(len(num2)-1,-1,-1):
            digit1 = 1
            tmp = 0
            for j in range(len(num1)-1,-1,-1):
                tmp = int(num1[j]) * int(num2[i]) * digit1 + tmp
                digit1 *= 10
            result += tmp * digit2
            digit2*=10
        return str(result)