class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenth_list = []
        for i in range(len(nums)):
            lenth_list.append(1)
            for n in range(i):
                if nums[n] < nums[i] and lenth_list[n] + 1 > lenth_list[i]:
                    lenth_list[i] = lenth_list[n] + 1
        max = 0
        for l in lenth_list:
            if l > max:
                max = l
        return max