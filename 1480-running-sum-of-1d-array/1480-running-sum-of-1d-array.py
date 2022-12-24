class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += nums[i-1] if i != 0 else 0
        return nums