class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        re = []
        for num in nums1:
            dict[num] = 1 if num not in dict else dict[num] + 1
        for num in nums2:
            if num in dict and dict[num] > 0:
                dict[num] = dict[num] - 1
                re.append(num)
        return re