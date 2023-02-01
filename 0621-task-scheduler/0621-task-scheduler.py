class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        units = 0
        count= Counter(tasks)
        for task in count:
            pq.append([-count[task],task])
        heapq.heapify(pq)
        while pq:
            temp = []
            for i in range(n+1):
                if pq:
                    popped = heapq.heappop(pq)
                    if -popped[0] > 1:
                        temp.append([popped[0]+1,popped[1]])
                if not pq and not temp:
                    return units + i+1
            units += n+1
            for ele in temp:
                heapq.heappush(pq,ele)
                      