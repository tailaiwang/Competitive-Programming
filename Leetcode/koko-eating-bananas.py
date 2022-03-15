#Koko Eating Bananas
#https://leetcode.com/problems/koko-eating-bananas/
#Medium (Daily Challenge), 20/01/2022
#Tailai Wang

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while (left < right):
            retval = (left + right) // 2
            amount = 0
            for pile in piles:
                amount += math.ceil(pile / retval)
            if amount > h:
                left = retval + 1
            else:
                right = retval
        return right
        
