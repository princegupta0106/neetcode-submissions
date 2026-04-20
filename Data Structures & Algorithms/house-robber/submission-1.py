class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [0]*n
        
        if n== 1:
            return nums[0]
        if n==2 :
            return max(nums)
        if n ==3:
            return max(nums[0]+ nums[2] , nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0]+ nums[2] , nums[1])
        for i in range(3, n):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-3] +nums[i-1])
        return dp[-1]

        