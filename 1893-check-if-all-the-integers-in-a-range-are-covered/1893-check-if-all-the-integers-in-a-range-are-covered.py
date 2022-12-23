class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for range in ranges:
            if left >= range[0] and left <= range[1]:
                left = range[1]+1
            if left > right:
                return True
        return False
