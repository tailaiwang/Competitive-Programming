#Permutation in String
#https://leetcode.com/problems/permutation-in-string/
#Medium (Daily Challenge), 11/02/2022
#Tailai Wang

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1 = Counter(s1)
        k = len(s1)
        n = len(s2)
        for i in range(n - k + 1):
            cur = Counter(s2[i:i+k])
            if len(cur - c1) == 0:
                return True
        return False
