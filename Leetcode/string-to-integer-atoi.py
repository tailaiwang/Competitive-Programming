<<<<<<< HEAD
#String to Integer (atoi)
#https://leetcode.com/problems/string-to-integer-atoi/
#Medium (Daily Challenge), 14/01/2022
#Tailai Wang

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        ls = list(s.strip())
        if len(ls) == 0 : return 0
        if ls[0] == "-":
            sign = -1
        else:
            sign = 1
        if (ls[0] == '+' or ls[0] == "-"):
            del(ls[0])
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
            
        return max(-2**31, min(sign * ret,2**31-1))
=======
#String to Integer (atoi)
#https://leetcode.com/problems/string-to-integer-atoi/
#Medium (Daily Challenge), 14/01/2022
#Tailai Wang

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        ls = list(s.strip())
        if len(ls) == 0 : return 0
        if ls[0] == "-":
            sign = -1
        else:
            sign = 1
        if (ls[0] == '+' or ls[0] == "-"):
            del(ls[0])
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
            
        return max(-2**31, min(sign * ret,2**31-1))
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
