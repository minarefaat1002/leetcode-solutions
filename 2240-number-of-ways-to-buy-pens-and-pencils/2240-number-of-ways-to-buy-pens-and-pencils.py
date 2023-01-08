class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        pens = 0
        ways = 0
        while True:
            pensCost = pens*cost1
            if pensCost > total:
                return ways
            pencils = int((total-pensCost)/cost2)
            pencilsCost = pencils*cost2
            ways += pencils + 1
            pens+=1
        return ways