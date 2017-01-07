class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        size = k if len(nums) - k > k else len(nums) - k
        for i in range(size):
            tmp = nums[i]
            nums[i] = nums[len(nums)-size + i]
            nums[len(nums)-size + i] = tmp
        if k > size:
            for j in range(size):
                tmp = nums.pop(0)
                nums.insert(k-1,tmp)
        else:
            index = len(nums)-k
            for j in range(k):
                tmp = nums.pop(index+j)
                nums.insert(k+j,tmp)