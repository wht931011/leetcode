class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # in d, key is sorted string, value is a list of original string
        d = {}
        re = []
        for str in strs:
            sort_str = "".join(sorted(str))
            if sort_str in d:
                d[sort_str].append(str)
            else:
                d[sort_str] = [str]
        for item in d:
            re.append(d[item])
        return re