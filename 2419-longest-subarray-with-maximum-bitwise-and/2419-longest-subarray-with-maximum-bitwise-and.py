class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        Max = max(nums)
        longest = 1
        i = 0
        while i < len(nums):
            count = 0
            while i<len(nums) and nums[i] == Max:
                count += 1
                i+=1
            i+=1
            longest = max(longest,count)
        return longest