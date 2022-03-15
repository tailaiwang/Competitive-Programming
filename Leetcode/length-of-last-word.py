#Length of Last Word
#https://leetcode.com/problems/length-of-last-word/
#Easy, 14/03/2022
#Tailai Wang

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(list(filter(bool, s.split(" ")))[-1])
        