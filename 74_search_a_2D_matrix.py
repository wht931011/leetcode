class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []: return False
        row_num = 0
        low, mid, high = 0, (len(matrix)-1)/2,len(matrix)-1
        while low <= high:
            if matrix[mid][0] > target:
                high = mid - 1
            elif (target >= matrix[mid][0] and mid + 1 == len(matrix)) or (target >= matrix[mid][0] and target < matrix[mid+1][0]):
                print(mid)
                row_num = mid
                break
            else:
                low = mid + 1
            mid = (low + high) / 2
        low, mid, high = 0, (len(matrix[0])-1)/2, len(matrix[0])-1
        while low<=high:
            if matrix[row_num][mid] > target:
                high = mid - 1
            elif matrix[row_num][mid] == target:
                return True
            else:
                low = mid + 1
            mid = (low + high) / 2
        return False