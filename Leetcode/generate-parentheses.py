<<<<<<< HEAD
#Generate Parentheses
#https://leetcode.com/problems/generate-parentheses/
#Medium, 07/01/2022
#Tailai Wang

class Solution(object):
    totalOutput = []
    totalN = 0
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.totalOutput = []
        self.totalN = n
        curParen = "("
        numOpen = 1
        numPairs = 0
        self.generateParenthesisHelp(curParen, numOpen, numPairs)
        return self.totalOutput
        
    def generateParenthesisHelp(self, curParen, numOpen, numPairs):
        if numPairs == self.totalN:
            if numOpen == 0:
                self.totalOutput.append(curParen)
        else:
            if numOpen == 0:
                numOpen = 1
                curParen += "("
                self.generateParenthesisHelp(curParen, numOpen, numPairs)
            else:
                closeParen = curParen + ")"
                openParen = curParen + "("
                self.generateParenthesisHelp(closeParen, numOpen - 1, numPairs + 1)
                if (numPairs + numOpen <= self.totalN):
                    self.generateParenthesisHelp(openParen, numOpen + 1, numPairs)

            
    
=======
#Generate Parentheses
#https://leetcode.com/problems/generate-parentheses/
#Medium, 07/01/2022
#Tailai Wang

class Solution(object):
    totalOutput = []
    totalN = 0
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.totalOutput = []
        self.totalN = n
        curParen = "("
        numOpen = 1
        numPairs = 0
        self.generateParenthesisHelp(curParen, numOpen, numPairs)
        return self.totalOutput
        
    def generateParenthesisHelp(self, curParen, numOpen, numPairs):
        if numPairs == self.totalN:
            if numOpen == 0:
                self.totalOutput.append(curParen)
        else:
            if numOpen == 0:
                numOpen = 1
                curParen += "("
                self.generateParenthesisHelp(curParen, numOpen, numPairs)
            else:
                closeParen = curParen + ")"
                openParen = curParen + "("
                self.generateParenthesisHelp(closeParen, numOpen - 1, numPairs + 1)
                if (numPairs + numOpen <= self.totalN):
                    self.generateParenthesisHelp(openParen, numOpen + 1, numPairs)

            
    
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
