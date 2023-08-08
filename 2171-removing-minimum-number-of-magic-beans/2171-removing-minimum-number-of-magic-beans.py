class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        totalBeans = sum(beans)
        beans.sort()
        minRemoved = float('inf')
        for i,b in enumerate(beans):
            minRemoved = min(minRemoved,totalBeans-(len(beans)-i)*b)
        return minRemoved