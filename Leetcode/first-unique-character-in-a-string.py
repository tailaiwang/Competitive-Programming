#First Unique Character in a String
#https://leetcode.com/problems/first-unique-character-in-a-string/
#Easy (Data Structures I), 25/03/2022
#Tailai Wang

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        thing = Counter(s)
        for i in range(len(s)):
            if thing[s[i]] == 1:
                return i
        return -1