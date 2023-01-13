class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        Sum = 0
        shortest = float('inf')
        for r in range(len(nums)):
            Sum += nums[r]
            while Sum >= target:
                Sum -= nums[l]
                shortest = min(shortest,r-l+1)
                l += 1
        return shortest if shortest != float('inf') else 0