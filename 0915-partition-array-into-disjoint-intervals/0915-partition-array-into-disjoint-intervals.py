class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        stack = [nums[-1]]
        for i in range(len(nums)-2,0,-1):
            stack.append(min(nums[i],stack[-1]))
        Max = nums[0]
        for i in range(1,len(nums)):
            if Max <= stack.pop():
                return i
            Max = max(Max,nums[i])
        