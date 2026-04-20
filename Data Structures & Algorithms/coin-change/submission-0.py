class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        n = len(coins)
        dp = [1000000]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)

        return -1 if dp[amount] == 1000000 else dp[-1]




