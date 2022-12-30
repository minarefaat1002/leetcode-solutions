class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(0)
        nums.insert(0,0)
        stack = []
        ans = 0
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                h = nums[stack.pop()]
                w = i - stack[-1] -1
                if k <= i-2 and k >= stack[-1]:
                    ans = max(ans, h * w)
            stack.append(i)
        nums.pop()
        return ans
