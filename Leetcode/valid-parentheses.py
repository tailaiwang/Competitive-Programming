#Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/
#Easy, 05/01/2022
#Tailai Wang

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openPars = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                openPars.append(char)
            else:
                if (len(openPars) <= 0):
                    return False
                if (char == ")" and openPars[len(openPars)-1] != "("):
                    return False
                elif (char == "]" and openPars[len(openPars)-1] != "["):
                    return False
                elif (char == "}" and openPars[len(openPars)-1] != "{"):
                    return False
                else:
                    openPars.pop()
        if len(openPars) != 0:
            return False
        return True
