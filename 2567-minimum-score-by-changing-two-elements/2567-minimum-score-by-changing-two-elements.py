class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-3]-nums[0] , nums[-1] - nums[2],nums[-2]-nums[1])