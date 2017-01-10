class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i ,j = 0, len(s)-1
        while i < len(s)/2 :
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        # convert list of str to a single str
        return ''.join(s)