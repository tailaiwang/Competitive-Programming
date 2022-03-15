<<<<<<< HEAD
#Is Subsequence
#https://leetcode.com/problems/is-subsequence/
#Easy (Daily Challenge), 02/03/2022
#Tailai Wang

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        for char in t:
            if char == s[0]:
                if len(s) == 1:
                    return True
                s = s[1:]
        return len(s) == 0
                
            
=======
#Is Subsequence
#https://leetcode.com/problems/is-subsequence/
#Easy (Daily Challenge), 02/03/2022
#Tailai Wang

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        for char in t:
            if char == s[0]:
                if len(s) == 1:
                    return True
                s = s[1:]
        return len(s) == 0
                
            
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
