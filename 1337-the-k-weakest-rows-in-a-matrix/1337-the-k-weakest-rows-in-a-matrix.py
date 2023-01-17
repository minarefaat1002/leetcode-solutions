class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def rightOne(row):
            l = 0 
            r = len(row)-1
            res = -1
            while l <= r:
                mid = (l+r)//2
                if row[mid] == 1:
                    res = mid
                    l = mid + 1
                elif row[mid] == 0:
                    r = mid - 1
            return res
        heap = []
        res = []
        heapq.heapify(heap)
        for i,row in enumerate(mat):
            n = rightOne(row) + 1
            heapq.heappush(heap,[n,i])
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res