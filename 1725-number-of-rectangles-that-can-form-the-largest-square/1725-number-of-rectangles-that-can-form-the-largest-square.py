class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        for sides in rectangles:
            maxLen = max(maxLen,min(sides))
        count = 0
        for sides in rectangles:
            if maxLen == min(sides):
                count+=1
        return count 