class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        Min1 = nums[0]
        Min2 = float('inf')
        for num in nums[1:]:
            if num <= Min1:
                Min1 = num
            elif num < Min2:
                Min2 = num
            elif num > Min2:
                return True
        return False