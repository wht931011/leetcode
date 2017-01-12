class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for s in magazine:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        for s in ransomNote:
            if s in d:
                d[s] -= 1
                if d[s] < 0:
                    return False
            else:
                return False
        return True