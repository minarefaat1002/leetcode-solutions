class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        Sum = 0
        shortest = 10**5 + 1
        for r in range(len(nums)):
            Sum += nums[r]
            while Sum >= target:
                Sum -= nums[l]
                shortest = min(shortest,r-l+1)
                l += 1
        return shortest if shortest != 100001 else 0