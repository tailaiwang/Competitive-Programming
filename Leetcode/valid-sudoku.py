#Valid Sudoku
#https://leetcode.com/problems/valid-sudoku/
#Medium, 03/01/2022
#Tailai Wang

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            complete = [False for x in range (9)]
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    if complete[int(cur) - 1]:
                        return False
                    else:
                        complete[int(cur) - 1] = True

        for i in range(9):
            complete = [False for x in range (9)]
            for j in range(9):
                cur = board[j][i]
                if cur != ".":
                    if complete[int(cur) - 1]:
                        return False
                    else:
                        complete[int(cur) - 1] = True

        hack = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
        for i in range(1,8,3):
            for j in range(1,8,3):
                complete = [False for x in range (9)]
                for x,y in hack:
                    cur = board[i + x][j + y]
                    if cur != ".":
                        if complete[int(cur) - 1]:
                            return False
                        else:
                            complete[int(cur) - 1] = True
        return True        
        
