class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        Min = float('inf')
        pivot = -1
        for i in range(len(points)):
            if points[i][0] == x and abs(points[i][1]-y) < Min:
                Min = abs(points[i][1]-y)
                pivot = i
            if points[i][1] == y and abs(points[i][0]-x) < Min:
                Min = abs(points[i][0]-x)
                pivot = i
        return pivot            
