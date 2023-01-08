class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        Max = 0
        for i in range(len(points)):
            hashMap = {}
            x1=points[i][0]
            y1 = points[i][1]
            for j in range(len(points)):
                if i == j:
                    continue
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 == x2:
                    hashMap[(x1)] = hashMap.get(x1,0) + 1
                    Max = max(Max,hashMap[x1])
                    continue
                slope = (y2-y1)/(x2-x1)
                intersect = y1 - slope*x1
                hashMap[(slope,intersect)] = hashMap.get((slope,intersect),0) + 1
                Max = max(Max,hashMap[(slope,intersect)])
        return Max + 1