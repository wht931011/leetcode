class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # refer: http://www.enjoyshare.org/detail/242106.html
        res = []
        c_map = [ 0 for _ in range(26)]
        for c in p:
            c_map[ord(c)- ord('a')] += 1
        left,right,count = 0,0,len(p)
        while right < len(s):
            index_right = ord(s[right]) - ord('a')
            index_left = ord(s[left]) - ord('a')
            c_map[index_right] -= 1
            if c_map[index_right] >= 0: count -= 1
            if right - left + 1 == len(p):
                if count == 0: res.append(left)
                if c_map[index_left] >=0: count += 1
                c_map[index_left] += 1
                left +=1
            right +=1
        return res
            