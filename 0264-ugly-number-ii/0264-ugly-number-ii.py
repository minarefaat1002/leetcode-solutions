class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # heap = [2,3,5]
        # last = 1
        # heapq.heapify(heap)
        # n-=1
        # while n:
        #     popped = heapq.heappop(heap)
        #     if popped == last:
        #         continue
        #     last = popped
        #     heapq.heappush(heap,popped*2)
        #     heapq.heappush(heap,popped*3)
        #     heapq.heappush(heap,popped*5)
        #     n-=1
        # return last
        dp = [0]*n
        dp[0] = 1
        i,j,z = 0,0,0
        for r in range(1,n):
            twoMultiple = dp[i]*2
            threeMultiple = dp[j]*3
            fiveMultiple = dp[z]*5
            dp[r] = min(twoMultiple,threeMultiple,fiveMultiple)
            if dp[r] == twoMultiple:
                i+=1
            if dp[r] == threeMultiple:
                j+=1
            if dp[r] == fiveMultiple:
                z+=1
        return dp[n-1]