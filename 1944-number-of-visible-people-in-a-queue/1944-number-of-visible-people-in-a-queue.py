class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        stack.append(heights[-1])
        res = [1]*len(heights)
        res[-1] = 0
        count = 0
        for i in range(len(heights)-2,-1,-1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            res[i] = count if count != 0 else 1
            stack.append(heights[i])
        return res