<<<<<<< HEAD
#Excel Sheet Column Number
#https://leetcode.com/problems/excel-sheet-column-number/
#Easy (Daily Challenge), 22/02/2022
#Tailai Wang

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        n = len(columnTitle) - 1
        retVal = 0
        for char in columnTitle:
            num = (ord(char) - 64)
            retVal += num * (26 ** n)
            n -= 1
        return retVal
=======
#Excel Sheet Column Number
#https://leetcode.com/problems/excel-sheet-column-number/
#Easy (Daily Challenge), 22/02/2022
#Tailai Wang

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        n = len(columnTitle) - 1
        retVal = 0
        for char in columnTitle:
            num = (ord(char) - 64)
            retVal += num * (26 ** n)
            n -= 1
        return retVal
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
