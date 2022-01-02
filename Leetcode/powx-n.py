#Pow(x,n)
#https://leetcode.com/problems/powx-n/
#Medium, 02/01/2022
#Tailai Wang

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n == 0):
            return 1
        if (n < 0):
            n = -n
            x = 1/x
        lower = self.myPow(x, n//2)
        if (n % 2 == 0):
            return lower * lower
        else:
            return lower * lower * x




