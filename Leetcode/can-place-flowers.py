#Can Place Flowers
#https://leetcode.com/problems/can-place-flowers/
#Easy (Daily Challenge), 18/01/2022
#Tailai Wang

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        prevFlower = 0
        nextFlower = 0
        for i in range (len(flowerbed)):
            if flowerbed[i] == 0:
                if i < len(flowerbed) - 1:
                    nextFlower = 1 if flowerbed[i + 1] == 1 else 0
                else:
                    nextFlower = 0
                if i > 0:
                    prevFlower = 1 if flowerbed[i - 1] == 1 else 0
                else:
                    prevFlower = 0
                if nextFlower == 0  and prevFlower == 0:
                    flowerbed[i] = 1
                    n -= 1
        return True if n <= 0 else False
