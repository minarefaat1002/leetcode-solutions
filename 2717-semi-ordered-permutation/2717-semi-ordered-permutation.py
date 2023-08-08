class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        minIndex = -1
        maxIndex = -1
        Min = float('inf')
        Max = float('-inf')
        for i,num in enumerate(nums):
            if num < Min:
                Min = num
                minIndex = i
            if num > Max:
                Max = num 
                maxIndex = i
        totalSwaps = minIndex + (len(nums) - maxIndex - 1)
        return totalSwaps if maxIndex > minIndex else totalSwaps - 1