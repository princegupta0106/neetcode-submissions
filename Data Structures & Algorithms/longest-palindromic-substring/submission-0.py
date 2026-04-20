class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s : return ''
        n = len(s)
        dp = [[False for _ in range(n)] for f in range (n)]
        # doing for len 1 
        for i in range(n):
            dp[i][i] = True
        ans = s[0]
        # doing for the rest of the length
        for length in range(2 , n+1):
            # i is the starting position and j is the ending 
            for i in range(0 , n-length+1):
                j = i + length -1
                if s[i] == s[j]:
                    if length ==2  or dp[i+1][j-1]:
                        dp[i][j] = True
                        if length > len(ans):
                            ans = s[i:j+1]
        return ans
        

        