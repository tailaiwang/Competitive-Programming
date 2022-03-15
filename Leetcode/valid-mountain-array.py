<<<<<<< HEAD
#Valid Mountain Array
#https://leetcode.com/problems/valid-mountain-array/
#Easy (Daily Challenge), 25/01/2022
#Tailai Wang



class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3 or arr[0]>arr[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(arr)):
            if uphill:
                if arr[i-1]>=arr[i]:
                    uphill = False
            if not uphill:
                if arr[i-1]<=arr[i]:
                    return False
        return not uphill
            
=======
#Valid Mountain Array
#https://leetcode.com/problems/valid-mountain-array/
#Easy (Daily Challenge), 25/01/2022
#Tailai Wang



class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3 or arr[0]>arr[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(arr)):
            if uphill:
                if arr[i-1]>=arr[i]:
                    uphill = False
            if not uphill:
                if arr[i-1]<=arr[i]:
                    return False
        return not uphill
            
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
