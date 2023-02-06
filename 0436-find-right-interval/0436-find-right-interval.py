class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:           
        res = []
        sortedIntervals = sorted([interval[0],interval[1],i] for i,interval in enumerate(intervals))
        for i,interval in enumerate(intervals):
            endI = interval[1]
            left = 0
            right = len(intervals)-1
            ans = -1
            while left <=right:
                mid = (left + right)//2
                if sortedIntervals[mid][0] >= endI:
                    ans = sortedIntervals[mid][2]
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(ans)
        return res