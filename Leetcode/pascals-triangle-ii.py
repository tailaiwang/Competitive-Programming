#Pascals Triangle II
#https://leetcode.com/problems/pascals-triangle-ii/
#Easy (Data Structures II), 18/04/2022
#Tailai Wang

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = []
        for i in range(rowIndex + 1):
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(output[i- 1][j] + output[i - 1][j - 1])
            output.append(tmp)
        return output[rowIndex]
            