class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]: continue
                s = nums[i]+nums[j]
                r = target - s
                left,right = j+1,len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == r:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and  nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] > r:
                        right-=1
                    else:
                        left+=1
        return res