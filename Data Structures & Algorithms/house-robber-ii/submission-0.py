class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1: return nums[0]
        if n ==2: return max(nums[0] , nums[1])

        res1 = -1
        dp = [0]*(n-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        for i in range(2 , n-1):
            dp[i] = max(dp[i-2]+nums[i] , dp[i-1])
        res1 = dp[-1]

        dp = [0]*(n-1)
        nums.reverse()

        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        for i in range(2 , n-1):
            dp[i] = max(dp[i-2]+nums[i] , dp[i-1])
        res2 = dp[-1]
        return max(res1,res2)




        






        