class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        subtract = 2147483647
        res = 0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            r = target - nums[i]
            left,right = i+1,len(nums)-1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == r:
                    return target
                elif sum > r:
                    if abs(sum - r) < subtract:
                        subtract = abs(sum - r)
                        res = sum + nums[i]
                    right-=1
                else:
                    if abs(sum - r) < subtract:
                        subtract = abs(sum - r)
                        res = sum + nums[i]
                    left+=1
        return res