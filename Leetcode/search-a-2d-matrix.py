#Search a 2D Matrix
#https://leetcode.com/problems/search-a-2d-matrix/
#Medium (Algorithm II), 18/03/2022
#Tailai Wang

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix) - 1
        n = len(matrix[0])
        l = 0 
        r = m
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if mid == m:
                break
            if matrix[mid][0] <= target and matrix[mid + 1][0] > target:
                break
            if matrix[mid][0] >= target:
                r = mid - 1
            else:
                print("here")
                l = mid + 1
        l = 0
        r = n - 1
        while l <= r:
            mid2 = (l + r) // 2
            if matrix[mid][mid2] == target:
                return True
            if matrix[mid][mid2] < target:
                l = mid2 + 1
            else:
                r = mid2 - 1
        return matrix[mid][0] == target