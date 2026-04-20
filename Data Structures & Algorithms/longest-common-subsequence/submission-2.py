class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for i in range(m+1)]
        dp2 = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp2[i+1][j+1] = 1
            dp[i][0] 
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] =  max( dp[i][j-1] , dp[i-1][j] ,dp[i-1][j-1] +dp2[i][j]) 
        return dp[-1][-1]
  
        # [0,0,0,0]
        # [0,0,0,0]
        # [0,0,0,0]

        dp2 
        # [0,0,0,0]
        # [0,0,1,1]
        # [0,0,1,1]
       
        




        