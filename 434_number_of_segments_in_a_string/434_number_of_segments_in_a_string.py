class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.split(' ')
        for w in s:
            if w != '':
                count += 1
        return count