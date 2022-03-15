#Word Pattern
#https://leetcode.com/problems/word-pattern/
#Easy (Daily Challenge), 17/01/2022
#Tailai Wang

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        patternDict ={}
        s = s.split()
        if (len(s) != len(pattern)):
            return False
        for i in range (len(pattern)):
            if (pattern[i] in patternDict):
                if patternDict[pattern[i]] != s[i]:
                    return False
            else:
                if (s[i] in patternDict.values()):
                    return False
                patternDict[pattern[i]] = s[i]
        return True
