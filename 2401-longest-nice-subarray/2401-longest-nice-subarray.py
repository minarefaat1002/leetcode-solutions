class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        AND = 0
        OR = 0
        res = 0
        for r in range(len(nums)):
            while OR&nums[r] != 0:
                OR = OR ^ nums[l]
                l+=1
            OR = OR | nums[r]
            res = max(res,r-l+1)
        return res