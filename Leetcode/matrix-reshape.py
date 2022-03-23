#Reshape the Matrix
#https://leetcode.com/problems/reshape-the-matrix/
#Easy (Data Structure I), 22/03/2022
#Tailai Wang

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        count = 0
        if m*n != r*c: return mat
        res = [[0] * c for _ in range(r)]
        for i, j in product(range(m), range(n)):
            res[count//c][count%c] = mat[i][j]
            count += 1      
        return res
