<<<<<<< HEAD
#Unique Paths
#https://leetcode.com/problems/unique-paths
#Medium, 10/01/2022
#Tailai Wang

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        output = [[0 for i in range (n)] for i in range (m)]
        output[0][0] = 1

        for i in range (n):
            output[0][i] = 1

        for i in range (m):
            output[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                output[j][i] = output[j][i - 1] + output[j - 1][i]

        return(output[m - 1][n - 1])
=======
#Unique Paths
#https://leetcode.com/problems/unique-paths
#Medium, 10/01/2022
#Tailai Wang

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        output = [[0 for i in range (n)] for i in range (m)]
        output[0][0] = 1

        for i in range (n):
            output[0][i] = 1

        for i in range (m):
            output[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                output[j][i] = output[j][i - 1] + output[j - 1][i]

        return(output[m - 1][n - 1])
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
