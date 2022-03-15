#Best Time Buy and Sell Stock II
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#Medium, 04/01/2022
#Tailai Wang

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        maxProfit = 0
        increasing = False
        curHold = -1
        for i in range (n):
            if (i < n - 1):
                if (prices[i] <= prices[i+1]):
                    if (not increasing): #time to buy
                        curHold = prices[i]
                        print("BUY", curHold)
                    increasing = True
                else:
                    if (increasing): #time to sell
                        maxProfit += prices[i] - curHold
                        curHold = -1
                        print("SELL", prices[i])
                    increasing = False

        if prices[n-1] > curHold and curHold != -1:
            maxProfit += prices[n-1] - curHold
            
        return maxProfit
