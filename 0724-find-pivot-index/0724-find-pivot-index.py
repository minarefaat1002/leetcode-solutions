class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        leftmostPivot = -1
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                leftmostPivot = i
                break
            leftSum+=nums[i]
        return leftmostPivot