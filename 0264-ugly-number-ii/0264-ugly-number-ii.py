class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [2,3,5]
        res = [1]
        heapq.heapify(heap)
        n-=1
        while n:
            popped = heapq.heappop(heap)
            if popped == res[-1]:
                continue
            res.append(popped)
            heapq.heappush(heap,popped*2)
            heapq.heappush(heap,popped*3)
            heapq.heappush(heap,popped*5)
            n-=1
        return res[-1]