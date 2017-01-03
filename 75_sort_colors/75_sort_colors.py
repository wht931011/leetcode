class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for n in nums:
            if n == 0: count[0] += 1
            if n == 1: count[1] += 1
            if n == 2: count[2] += 1
        n = 0
        for i in range(len(count)):
            while count[i]>0:
                nums[n] = i
                n+=1
                count[i]-=1