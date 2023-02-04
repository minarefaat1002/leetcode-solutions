class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10**10
        res = -1
        while left <= right:
            time = 0
            mid = (left+right)//2
            for i in range(len(dist)):
                d = dist[i]
                if i == len(dist) - 1:
                    time += (d/mid)
                else:
                    time += ((d-1)//mid) + 1
            if time <= hour:
                res = mid 
                right = mid - 1
            else:
                left = mid + 1
        return res