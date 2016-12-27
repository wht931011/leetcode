class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split('.'), version2.split('.')
        size = len(v1) if len(v1) < len(v2) else len(v2)
        for i in range(size):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                continue
        if len(v1) < len(v2):
            for i in range(len(v2)-1, len(v1)-1,-1):
                if int(v2[i]) > 0:
                    return -1
            return 0
        elif len(v2) < len(v1):
            for i in range(len(v1)-1, len(v2)-1,-1):
                if int(v1[i]) > 0:
                    return 1
            return 0
        else:
            return 0
                