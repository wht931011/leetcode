class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def search(s,start,end,result):
            if len(s[start:end+1])>len(result):
                    result = s[start:end+1]
            while start-1>=0 and end+1<len(s):
                if s[start-1] == s[end+1]:
                    if len(s[start-1:end+1+1])>len(result):
                        result = s[start-1:end+1+1]
                    start-=1
                    end+=1
                else:
                    break
            return result

        result = ''
        for i in range(len(s)):
            result = search(s,i,i,result)
            if i+1<len(s) and s[i] == s[i+1]:
                result = search(s,i,i+1,result)
        return result
                