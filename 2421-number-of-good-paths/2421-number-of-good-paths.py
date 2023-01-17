class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        if len(vals) == 1:
            return 1
        parent = [i for i in range(len(vals))]
        rank = [1]*len(vals)
        res = len(vals)
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        activated = [False]*len(vals)
        valToNode = {}
        for vertex,val in enumerate(vals):
            if val not in valToNode:
                valToNode[val] = []
            valToNode[val].append(vertex)
        sortedValToNode = {}
        keys = list(valToNode.keys())
        keys.sort()
        for key in keys:
            sortedValToNode[key] = valToNode[key]
        for val in sortedValToNode:
            indexes = sortedValToNode[val]
            for index in indexes:
                for neighbor in graph[index]:
                    if activated[neighbor]:
                        union(index,neighbor)
                activated[index] = True
            count = {}
            for index in indexes:
                count[find(index)] = count.get(find(index),0) + 1
            for item in count:
                res += count[item]*(count[item]-1)//2
        return res