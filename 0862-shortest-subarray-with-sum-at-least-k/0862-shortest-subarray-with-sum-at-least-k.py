from collections import deque 
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        d = deque([[-1,0]])
        Sum = 0
        shortest = 100001
        for i in range(len(nums)):
            Sum+=nums[i]
            while d and Sum <= d[-1][1]:
                d.pop()
            d.append([i,Sum])
            while d and Sum-d[0][1] >= k:
                popped = d.popleft()
                shortest = min(shortest,i-popped[0])
        return shortest if shortest!=100001 else -1
