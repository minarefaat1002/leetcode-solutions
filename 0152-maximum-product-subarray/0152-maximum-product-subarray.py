class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        curMax=nums[0]
        curMin = nums[0]
        for i in range(1,len(nums)):
            tmp = curMax
            n= nums[i]
            curMax = max(n*curMax , n*curMin , n) # n for input like that [-1,8]
            curMin = min(tmp*n,n*curMin,n) # n for input like that [-1,-8]
            res = max(curMax,res)
        return res