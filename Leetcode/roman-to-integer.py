#Roman to Integer
#https://leetcode.com/problems/roman-to-integer/
#Easy, 16/01/2022
#Tailai Wang

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        i = 0
        while i < (len(s)):
            if (i == len(s) - 1):
                if s[len(s) - 1] == "I": sum += 1
                if s[len(s) - 1] == "V": sum += 5
                if s[len(s) - 1] == "X": sum += 10
                if s[len(s) - 1] == "L": sum += 50
                if s[len(s) - 1] == "C": sum += 100
                if s[len(s) - 1] == "D": sum += 500
                if s[len(s) - 1] == "M": sum += 1000
                break
            if s[i] == "I":
                if s[i + 1] == "V":
                    sum += 4
                    i += 1
                elif s[i + 1] == "X":
                    sum += 9
                    i += 1
                else:
                    sum += 1
            elif s[i] == "V":
                sum += 5
            elif s[i] == "X":
                if s[i + 1] == "L":
                    sum += 40
                    i += 1
                elif s[i + 1] == "C":
                    sum += 90
                    i += 1
                else:
                    sum += 10
            elif s[i] == "L":
                sum += 50
            elif s[i] == "C":
                if s[i + 1] == "D":
                    sum += 400
                    i += 1
                elif s[i + 1] == "M":
                    sum += 900
                    i += 1
                else:
                    sum += 100
            elif s[i] == "D":
                sum += 500
            else:
                sum += 1000
            i += 1
        
        
        return sum
        
