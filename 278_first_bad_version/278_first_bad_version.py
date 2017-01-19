# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mid = (start + end) / 2 will cause overflow
        # if start+end > intMax
        # so use mid = start + (end-start)/2
        start,mid,end = 0,n/2,n
        while end-start>1:
            
            if isBadVersion(mid):
                end = mid
                mid = end/2
            else:
                start = mid
                mid = start+(end-start)/2
                
        return end