class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        Max = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r
                l+=1
            Max = max(Max,r-l+1)
        return Max
