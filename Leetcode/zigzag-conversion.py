<<<<<<< HEAD
#ZigZag Conversion
#https://leetcode.com/problems/zigzag-conversion/
#Medium, 01/01/2022
#Tailai Wang

class Solution(object):
    def convert(self, s, numRows):
        output = ""
        rowList = [output for i in range(numRows)]
        rowCounter = 1
        decreasing = False

        if numRows == 1:
            rowList = [s]
        else:
            for char in range(len(s)):
                rowList[rowCounter - 1] = rowList[rowCounter - 1] + s[char]
                if (rowCounter == numRows):
                    decreasing = True
                if (rowCounter == 1):
                    decreasing = False
                if not decreasing:
                    rowCounter += 1
                else:
                    rowCounter -= 1

        for row in rowList:
            output += row

        return output
=======
#ZigZag Conversion
#https://leetcode.com/problems/zigzag-conversion/
#Medium, 01/01/2022
#Tailai Wang

class Solution(object):
    def convert(self, s, numRows):
        output = ""
        rowList = [output for i in range(numRows)]
        rowCounter = 1
        decreasing = False

        if numRows == 1:
            rowList = [s]
        else:
            for char in range(len(s)):
                rowList[rowCounter - 1] = rowList[rowCounter - 1] + s[char]
                if (rowCounter == numRows):
                    decreasing = True
                if (rowCounter == 1):
                    decreasing = False
                if not decreasing:
                    rowCounter += 1
                else:
                    rowCounter -= 1

        for row in rowList:
            output += row

        return output
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
