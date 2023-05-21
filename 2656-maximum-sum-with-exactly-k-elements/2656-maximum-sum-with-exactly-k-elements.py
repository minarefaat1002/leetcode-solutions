class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        Max = max(nums)
        result = 0
        for i in range(Max,Max+k):
            result += i
        return result