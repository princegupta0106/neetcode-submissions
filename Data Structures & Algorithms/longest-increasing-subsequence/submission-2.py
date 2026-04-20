class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float('inf')]*(len(nums)+1)
        dp[0] = nums[0]
        res = 0
        for x in nums:
            temp = 1 
            for i in range(res,-1, -1):
                if dp[i] < x:  
                    break 
            dp[i+1] = min(dp[i+1], x)
            temp = i+1
            res = max(res, temp)
        return res
        



        