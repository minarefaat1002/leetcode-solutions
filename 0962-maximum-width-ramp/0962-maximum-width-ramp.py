class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [[nums[0],0]]
        for i in range(1,len(nums)):
            num = nums[i]
            if stack[-1][0] > num:
                stack.append([num,i])
        res = -1
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            while stack and stack[-1][0] <= num:
                popped = stack.pop()
                res = max(res,i-popped[1])
        return res if res != 100000 else 0
                