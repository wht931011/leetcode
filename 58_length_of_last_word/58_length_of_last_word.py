class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.replace(' ','') == '':
            return 0
        s_list = s.split(' ')
        for i in range(len(s_list)-1,-1,-1):
            if s_list[i] != '':
                return len(s_list[i])