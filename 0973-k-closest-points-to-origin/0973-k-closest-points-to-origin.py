class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for point in points:
            x= point[0]
            y = point[1]
            distances.append([x,y,math.sqrt(x**2+y**2)])
        distances.sort(key = lambda x: -x[2])  # minus here is for the decreasing order 
        for i in range(k):
            res.append(distances.pop()[0:2])
        return res
            