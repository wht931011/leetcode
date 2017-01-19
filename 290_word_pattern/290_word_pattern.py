class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        d = {}
        str = str.split(' ')
        if len(str)!=len(pattern): return False
        print(str)
        for i in range(len(str)):
            if str[i] not in d:
                if pattern[i] not in d.values():
                    d[str[i]] = pattern[i]
                else:
                    return False
            else:
                if d[str[i]] != pattern[i]: return False
        return True
        