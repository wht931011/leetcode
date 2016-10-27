class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = len(a) - 1
        b1 = len(b) - 1
        carry = 0
        re = ''
        while a1 >= 0 or b1 >= 0:
            m = int(a[a1]) if a1>=0 else 0
            n = int(b[b1]) if b1>=0 else 0
            # when 0 + 0, carry = 0, put 1 (0 % 2 = 0). carry = 0 (0 / 2 = 0)
            # when 1 + 1, carry = 1, put 1 (3 % 2 = 1). carry = 1 (3 / 2 = 1)
            # when 1 + 1. carry = 0, put 0 (2 % 2 = 0). carry = 1 (2 / 2 = 1)
            # when 1 + 0 or 0 + 1, carry = 0 put 1 (1 % 2 = 1). carry = 0 (1 / 2 = 0)
            # when 1 + 0 or 0 + 1, carry = 1 put 0 (2 % 2 = 0). carry = 1 (2 / 2 = 1)
            re = '0' + re if (m + n + carry) % 2 == 0 else '1' + re
            carry = 0 if (m + n + carry) / 2 == 0 else 1
            a1 -= 1
            b1 -= 1
        if carry == 1: re = '1' + re
        return re