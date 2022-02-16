#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Medium, 16/02/2022
#Tailai Wang

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = ''
        mx = 0
        for c in s:
            if c not in seen:
                seen+=c
            else:
                seen = seen[seen.index(c) + 1:] + c
            mx = max(mx, len(seen))
        return mx
