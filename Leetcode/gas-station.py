#Gas Station
#https://leetcode.com/problems/gas-station/
#Medium (Daily Challenge), 21/01/2022
#Tailai Wang


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) < sum(cost)):
            return -1
        
        tank = 0
        retVal = 0
        n = len(gas)
        
        for i in range(n):
            tank += gas[i] - cost[i]
            
            if tank < 0:
                retVal = i+1
                tank = 0
            
        return retVal
