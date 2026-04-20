class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [True]*(n+2) 
        arr[0] = False
        for x in nums:
            if x  >=0 and x  <= n:
                arr[x] = False
        for i, x in enumerate(arr):
            if x :
                return i 
        

        