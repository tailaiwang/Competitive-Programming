<<<<<<< HEAD
#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/
#Easy, 22/01/2022
#Tailai Wang

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long = ""
        index = 0
        short = 200
        for word in strs:
            if len(word) < short:
                short = len(word)
                
    
        while True:
            cur =""
            if index == short:
                break
            for word in strs:
                if cur == "":
                    cur = word[index]
                else:
                    if word[index] != cur:
                        return long
            index += 1
            long += cur
        return long
=======
#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/
#Easy, 22/01/2022
#Tailai Wang

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long = ""
        index = 0
        short = 200
        for word in strs:
            if len(word) < short:
                short = len(word)
                
    
        while True:
            cur =""
            if index == short:
                break
            for word in strs:
                if cur == "":
                    cur = word[index]
                else:
                    if word[index] != cur:
                        return long
            index += 1
            long += cur
        return long
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
