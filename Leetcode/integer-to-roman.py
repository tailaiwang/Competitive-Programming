#Integer to Roman
#https://leetcode.com/problems/integer-to-roman/
#Medium, 17/01/2022
#Tailai Wang


# Use a dictionary to make it prettier
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        curString = ""
        def helper (curString, num):
            if (num == 0):
                return curString
            if (num >= 1000):
                return helper(curString+("M" * (num // 1000)) , num % 1000)
            elif (num >= 900):
                return helper(curString+("CM" * (num // 900)), num % 900)
            elif (num >= 500):
                return helper(curString+("D" * (num // 500)), num % 500)
            elif (num >= 400):
                return helper(curString+("CD" * (num // 400)), num % 400)
            elif (num >= 100):
                return helper(curString+("C" * (num // 100)), num % 100)
            elif (num >= 90):
                return helper(curString+("XC" * (num // 90)), num % 90)
            elif (num >= 50):
                return helper(curString+("L" * (num // 50)), num % 50)
            elif (num >= 40):
                return helper(curString+("XL" * (num // 40)), num % 40)
            elif (num >= 10):
                return helper(curString+("X" * (num // 10)), num % 10)
            elif (num >= 9):
                return helper(curString+("IX" * (num // 9)), num % 9)
            elif (num >= 5):
                return helper(curString+("V" * (num // 5)), num % 5)
            elif (num >= 4):
                return helper(curString+("IV" * (num // 4)), num % 4)
            else:
                return helper(curString+("I" * num), 0)
        return helper(curString, num)
    
    
   
