class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 0
        j = 1
        count = 0
        while j < len(intervals):
            if min(intervals[i][1] , intervals[j][1]) > max(intervals[i][0],intervals[j][0]):
                count += 1
                if intervals[i][1] < intervals[j][1]:
                    j += 1
                else:
                    i = j
                    j += 1
            else:
                i = j
                j+=1
        return count