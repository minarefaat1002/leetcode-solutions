class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        height.insert(0,0)
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
