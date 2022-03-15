#Best Time Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Easy, 04/01/2022
#Tailai Wang

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if (price < minPrice):
                minPrice = price
            profit = price - minPrice
            if (profit > maxProfit):
                maxProfit = profit

        return maxProfit
