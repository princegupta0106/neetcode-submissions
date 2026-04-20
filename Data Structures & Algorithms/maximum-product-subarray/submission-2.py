class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def handleArray(arr):
            if not arr :
                return 0
            negs = []
            for i , x in enumerate(arr):
                
                if x < 0: 
                    negs.append(i)
            if not negs  or not len(negs)%2:
                res = 1
                for x in arr:
                    res*= x
                return res   
            res1 = arr[negs[-1]]
            if   negs[-1] > 0:
                res1 = 1 
                for i in range(negs[-1]):
                    res1*= arr[i]
            res2 = arr[negs[0]]
            if negs[0]+1 < len(arr):
                res2  = 1
                for i in range(negs[0]+1 , len(arr)):
                    res2 *= arr[i]
            return max(res1, res2)
        arr = []
        res = nums[0]
        for x in nums:
            if not x :
                res = max(res, handleArray(arr) ,0 ) 
                arr = []
            else:
                arr.append(x)
        res = max(res, handleArray(arr)) 
        return res

        


