class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        hashMap = collections.defaultdict(list)
        visitedStops = set()
        visitedRoutes = set()
        for i in range(len(routes)):
            for stop in routes[i]:
                hashMap[stop].append(i)
        q = deque()
        q.append([source,0])
        visitedStops.add(source)
        while q:
            stop,moves = q.popleft()
            for route in hashMap[stop]:
                if route in visitedRoutes:
                    continue
                visitedRoutes.add(route)
                for s in routes[route]:
                    if s not in visitedStops:
                        if s == target:
                            return moves+1
                        q.append([s,moves+1])
        return -1