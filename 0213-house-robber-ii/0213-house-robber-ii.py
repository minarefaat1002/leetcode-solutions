class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            rob1 , rob2 = 0 , 0
            for num in nums:
                temp = max(rob2,rob1+num)
                rob1 = rob2
                rob2 = temp 
            return rob2
        return max(rob(nums[1:]),rob(nums[:-1])) if len(nums) > 1 else nums[0]