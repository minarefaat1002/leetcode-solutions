class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        point1 = points[0]
        point2 = points[1]
        point3 = points[2]
        return (point1[1]-point2[1])*(point2[0]-point3[0]) != (point1[0]-point2[0])*(point2[1]-point3[1])
            