class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = set()
        sumNums = sum(nums)
        sums.add(0)
        if sumNums%2 :
            return False
        for x in nums :
            temp = []
            for s in sums :
                temp.append(x+s)
            sums.update(temp)
        return sumNums/2 in sums 

            


            


        