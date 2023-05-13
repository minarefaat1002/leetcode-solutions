class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        i = len(nums[0])-1
        score = 0 
        for j in range(i,-1,-1):
            Max = -1
            for z in range(len(nums)):
                Max = max(Max,nums[z][j])
            score += Max
        return score