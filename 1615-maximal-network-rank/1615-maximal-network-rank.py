class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = {}
        maxRank = 0
        for road in roads:
            count[road[0]] = count.get(road[0],0) + 1
            count[road[1]] = count.get(road[1],0) + 1
        roads = set(tuple(road) for road in roads)
        for i in range(n):
            for j in range(i+1,n):
                maxRank = max(count.get(i,0) + count.get(j,0) - ( 1 if (i,j) in roads or (j,i) in roads else 0) ,maxRank) 
        return maxRank