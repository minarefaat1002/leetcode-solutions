class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hashMap = {}
        for i,interval in enumerate(intervals):
            hashMap[(interval[0],interval[1])] = i            
        res = []
        sortedIntervals = sorted(intervals)
        for i,interval in enumerate(intervals):
            endI = interval[1]
            left = 0
            right = len(intervals)-1
            ans = -1
            while left <=right:
                mid = (left + right)//2
                if sortedIntervals[mid][0] >= endI:
                    ans = hashMap[(sortedIntervals[mid][0],sortedIntervals[mid][1])]
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(ans)
        return res