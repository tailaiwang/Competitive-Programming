#Pascal's Triangle
#https://leetcode.com/problems/pascals-triangle/
#Easy (Data Structures I), 22/03/2022
#Tailai Wang

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range (numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                tmp = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        tmp.append(1)
                    else:
                        tmp.append(res[i-1][j-1] + res[i-1][j])
                res.append(tmp)
        return res