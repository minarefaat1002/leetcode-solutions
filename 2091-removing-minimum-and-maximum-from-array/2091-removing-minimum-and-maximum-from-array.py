class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        pivotMin = -1
        pivotMax = -1
        Min = float('inf')
        Max = float('-inf')
        for i,num in enumerate(nums):
            if num < Min:
                Min = num
                pivotMin = i
            if num > Max:
                Max = num
                pivotMax = i
        return min(max(pivotMin,pivotMax)+1 , len(nums) - min(pivotMin,pivotMax),min(pivotMin,pivotMax)+1 + len(nums)-max(pivotMin,pivotMax))