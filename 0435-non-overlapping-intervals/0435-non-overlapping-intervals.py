class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 0
        count = 0
        for j in range(1,len(intervals)):
            if min(intervals[i][1] , intervals[j][1]) > max(intervals[i][0],intervals[j][0]):
                count += 1
            else:
                i = j
            if intervals[i][1] > intervals[j][1]:
                i = j
        return count