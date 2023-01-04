class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = 0
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp = dp + 1
                ans += dp
            else:
                dp = 0
        return ans