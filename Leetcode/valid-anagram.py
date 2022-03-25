#Valid Anagram
#https://leetcode.com/problems/valid-anagram/
#Easy (Data Structures I), 25/03/2022
#Tailai Wang

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)