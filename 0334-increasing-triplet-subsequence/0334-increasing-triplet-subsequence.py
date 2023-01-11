class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        Min1 = float('inf')
        Min2 = float('inf')
        for num in nums:
            if num <= Min1:
                Min1 = num
            elif num <= Min2:
                Min2 = num
            else:
                return True
        return False