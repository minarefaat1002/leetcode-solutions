class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(node,d):
            q = deque()
            q.append([node,0]) # node ===> dist
            visited = set()
            visited.add(node)
            while q:
                node,dist = q.popleft()
                d[node] = dist
                if edges[node] in visited:
                    continue
                if edges[node] != -1:
                    q.append([edges[node],dist+1])
                    visited.add(edges[node])
        dist1 = {}
        dist2 = {}
        bfs(node1,dist1)
        bfs(node2,dist2)
        Min = len(edges) + 1
        node = -1
        for item in dist1:
            if item in dist2:
                if Min >= max(dist1[item],dist2[item]):
                    node = item if Min != max(dist1[item],dist2[item]) else min(item,node)
                    Min = max(dist1[item],dist2[item])
        return node