class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heap = []
        minCost = 0
        heapq.heapify(heap)
        for cost in costs:
            heapq.heappush(heap,(cost[1]-cost[0],cost[0],cost[1]))
        for i in range(len(costs)//2):
            diff,costA,costB = heapq.heappop(heap)
            minCost+=costB
        for i in range(len(costs)//2):
            diff,costA,costB = heapq.heappop(heap)
            minCost+=costA
        return minCost