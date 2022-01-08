#Combination Sum
#https://leetcode.com/problems/combination-sum/
#Medium, 08/01/2022
#Tailai Wang

class Solution(object):
    solution = []
    target = 0
    def combinationSumHelp(self, candidates, curSol, curSum):
        if (sum(curSol) == self.target):
            self.solution.append(curSol[:])
            return
        elif (sum(curSol) > self.target):
            return
        else:
            for i in range (curSum, len(candidates)):
                curSol.append(candidates[i])
                self.combinationSumHelp(candidates, curSol, i)
                curSol.pop()
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.solution = []
        self.target = target
        self.combinationSumHelp(candidates, [], 0)
        return self.solution
