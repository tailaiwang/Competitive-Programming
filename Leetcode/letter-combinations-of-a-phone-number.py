<<<<<<< HEAD
#Letter Combinations of a Phone Number
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#Medium, 10/03/2022
#Tailai Wang

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': "abc", '3': "def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        output = []
        if digits == "":
            return output
        def helper(digits, cur):
            if digits == "":
                output.append(cur)
            else:
                char = digits[0]
                digits = digits[1:]
                possibilities = mapping[char]
                for letter in possibilities:
                    helper(digits, cur+letter)        
        helper(digits, "")
        return output
                
            
        
=======
#Letter Combinations of a Phone Number
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#Medium, 10/03/2022
#Tailai Wang

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': "abc", '3': "def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        output = []
        if digits == "":
            return output
        def helper(digits, cur):
            if digits == "":
                output.append(cur)
            else:
                char = digits[0]
                digits = digits[1:]
                possibilities = mapping[char]
                for letter in possibilities:
                    helper(digits, cur+letter)        
        helper(digits, "")
        return output
                
            
        
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
