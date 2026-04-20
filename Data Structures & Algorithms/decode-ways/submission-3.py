class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] =='0': 
            return 0
        prev2, prev1 = 1 ,1
        for i in range(1, len(s)):
            temp = 0 
            if s[i-1] =='2' and s[i] >='0' and s[i]<='6':
                temp+=prev2 
            elif s[i-1] =='1' :
                temp+=prev2 
            elif s[i] != '0' :
                pass
            else:
                return 0
            if s[i] != '0' :
                temp+= prev1    
            prev2= prev1
            prev1 = temp
        return prev1 
                


        