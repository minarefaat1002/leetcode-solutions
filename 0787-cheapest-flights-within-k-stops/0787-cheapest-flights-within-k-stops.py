class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        Min = [float('inf')]*(n+1)
        graph = collections.defaultdict(list)
        for flight in flights:
            graph[flight[0]].append([flight[1],flight[2]])
        q = deque()
        q.append([src,0,0]) # curNode , price , moves
        cheapest = float('inf')
        while q:
            cur,curPrice,moves = q.popleft()
            if moves > k+1 or curPrice > cheapest:
                continue
            if curPrice < Min[cur]:
                Min[cur] = curPrice
            else:
                continue
            if cur == dst and curPrice < cheapest:
                cheapest = curPrice
            for child in graph[cur]:
                q.append([child[0],curPrice+child[1],moves+1])
        return cheapest if cheapest != float('inf') else -1