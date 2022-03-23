#Backspace String Compare
#https://leetcode.com/problems/backspace-string-compare/
#Easy (Algorithms II), 22/03/2022
#Tailai Wang

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "#":
                if i > 0:
                    s = s[:i - 1] + s[i + 1:]
                    n -= 2
                    i -= 2
                else:
                    s = s[1:]
                    n -= 1
                    i -= 1
            i += 1
            
        n = len(t)
        i = 0
        while i < n:
            if t[i] == "#":
                if i > 0:
                    t = t[:i - 1] + t[i + 1:]
                    n -= 2
                    i -= 2
                else:
                    t = t[1:]
                    n -= 1
                    i -= 1
            i += 1
        
        print(s, t)
        return s == t