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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rectangles = [0]*len(matrix[0])
        maxArea = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    rectangles[j] = 0
                else:
                    rectangles[j] += int(matrix[i][j])
            maxArea = max(self.largestRectangleArea(rectangles.copy()),maxArea)
        return maxArea
            