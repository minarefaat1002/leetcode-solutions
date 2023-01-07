class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [2,3,5]
        last = 1
        heapq.heapify(heap)
        n-=1
        while n:
            popped = heapq.heappop(heap)
            if popped == last:
                continue
            last = popped
            heapq.heappush(heap,popped*2)
            heapq.heappush(heap,popped*3)
            heapq.heappush(heap,popped*5)
            n-=1
        return last