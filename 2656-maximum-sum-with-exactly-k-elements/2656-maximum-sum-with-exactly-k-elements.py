class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        Max = max(nums)
        return k*(2*Max+k-1)//2