<<<<<<< HEAD
#Find All Anagrams in a String
#https://leetcode.com/problems/find-all-anagrams-in-a-string/
#Medium (Daily Challenge), 02/02/2022
#Tailai Wang

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        
        p = Counter(p)                    
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])   
            else:    
                window[s[i-1]] -= 1       
                window[s[i+m-1]] += 1     
            if len(window - p) == 0:      
                ans.append(i)
                
        return ans
=======
#Find All Anagrams in a String
#https://leetcode.com/problems/find-all-anagrams-in-a-string/
#Medium (Daily Challenge), 02/02/2022
#Tailai Wang

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        
        p = Counter(p)                    
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])   
            else:    
                window[s[i-1]] -= 1       
                window[s[i+m-1]] += 1     
            if len(window - p) == 0:      
                ans.append(i)
                
        return ans
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
