class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1
        for i in range(len(nums)):
            if abs(nums[i]) < len(nums)+1:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1