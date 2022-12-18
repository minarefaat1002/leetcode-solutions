class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i , t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stacktemp , stackindex = stack.pop()
                res[stackindex] = (i-stackindex)
            stack.append([t,i])
        return res 