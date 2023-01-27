class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        t = tasks[0][0]
        heap = [] # processing time , index , enqueue time
        i = 0
        res = []
        while i < len(tasks) or heap:
            while i<len(tasks) and tasks[i][0] <= t:
                heapq.heappush(heap,[tasks[i][1],tasks[i][2],tasks[i][0]])
                i += 1
            if not heap:
                t = tasks[i][0]
                continue
            popped = heapq.heappop(heap)
            res.append(popped[1])
            t += popped[0]
        return res
                
                