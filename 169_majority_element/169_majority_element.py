class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for x in nums:
            if x in dict:
                dict[x] +=1
            else:
                dict[x] = 1
        size = len(nums)/2
        for e in dict.keys():
            if dict[e] > size:
                return e
            