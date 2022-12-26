class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        moves = 0
        for i in range(1,len(nums)):
            cur = nums[i]
            if cur <= prev:
                moves += prev - cur + 1
                cur = prev + 1
            prev = cur
        return moves
            