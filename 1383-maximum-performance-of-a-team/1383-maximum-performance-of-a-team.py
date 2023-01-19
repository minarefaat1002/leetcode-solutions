class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiencySpeed = []
        speedSum = 0
        MOD = 10**9 + 7
        heap = []
        for i in range(n):
            efficiencySpeed.append([efficiency[i],speed[i]])
        efficiencySpeed.sort(reverse = True)
        res = -1
        heapq.heapify(heap)
        for i in range(n):
            minEfficiency = efficiencySpeed[i][0]
            speedSum += efficiencySpeed[i][1]
            if len(heap) < k:
                heapq.heappush(heap,efficiencySpeed[i][1])
            else:
                speedSum -= heapq.heappop(heap)
                heapq.heappush(heap,efficiencySpeed[i][1])
            res = max(res,minEfficiency*speedSum)
        return res%MOD
            