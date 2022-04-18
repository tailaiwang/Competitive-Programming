#Add Digits
#https://leetcode.com/problems/add-digits/
#Easy (Daily Challenge), 07/02/2022
#Tailai Wang


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
