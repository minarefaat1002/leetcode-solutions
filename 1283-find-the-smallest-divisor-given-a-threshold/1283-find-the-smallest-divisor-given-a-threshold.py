class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        res = float('inf')
        while left <= right:
            mid = (left+right)//2
            Sum = 0
            for num in nums:
                Sum += (num-1)//mid + 1
            if Sum <= threshold:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res