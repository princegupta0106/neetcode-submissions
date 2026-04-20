class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for  i in range(n):
            j = 0 
            while i+ j < n and i - j >=0 :
                if s[i+j] == s[i-j]:
                    res +=1 
                else :
                    break
                j+=1 
        
        for i in range(n-1):
            k = i+1
            j = 0 
            while k+ j < n and i - j >=0 :
                if s[k+j] == s[i-j]:
                    res +=1 
                else :
                    break
                j+=1 
        return res
            
        