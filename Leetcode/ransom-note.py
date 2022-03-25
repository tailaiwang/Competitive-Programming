#Ransome Note
#https://leetcode.com/problems/ransom-note/
#Easy (Data Structures I), 25/03/2022
#Tailai Wang

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return len((Counter(ransomNote) - Counter(magazine))) == 0
