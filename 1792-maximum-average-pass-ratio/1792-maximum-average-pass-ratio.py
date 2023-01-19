class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for c in classes:
            heap.append((c[0]/c[1] - (c[0]+1) / (c[1]+1),c[0],c[1]))
        heapq.heapify(heap)
        while extraStudents:
            popped = heapq.heappop(heap)
            new = ((popped[1]+1)/(popped[2]+1)-(popped[1]+2)/(popped[2]+2),popped[1]+1,popped[2]+1)
            heapq.heappush(heap,new)
            extraStudents -= 1
        return sum(a/b for v,a,b in heap)/len(heap)
        