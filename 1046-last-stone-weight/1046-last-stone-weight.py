class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones =[-s for s in stones] # we used minus values cause we will use min heap cause python doesn't have max heap
        heapq.heapify(stones)
        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first-second)
        stones.append(0)  # if there is not stones in the list return 0    
        return abs(stones[0]) # to return the positive value 
    # time complexity is O(nlogn) and space complexity is O(n)