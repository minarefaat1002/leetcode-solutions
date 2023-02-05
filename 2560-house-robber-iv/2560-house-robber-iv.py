class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def helper(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i+=1
            return count 
                    
        
        left = min(nums)
        right = max(nums)
        res = 0
        while left <= right:
            mid = (left + right)//2
            if helper(mid) >= k:
                res = mid 
                right = mid - 1
            else:
                left = mid + 1
        return res