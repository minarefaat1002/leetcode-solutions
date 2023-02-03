class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        res = -1
        while l <= r:
            mid = (l+r)//2
            k = maxOperations
            for num in nums:
                k -= ((num-1)//mid)
            if k >= 0:
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res
            
            