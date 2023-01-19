class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = {}
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = []
            graph[ticket[0]].append(ticket[1])
        res = ["JFK"]
        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in graph:
                return False
            for i in range(len(graph[cur])):
                d = graph[cur].pop(i)
                res.append(d)
                if dfs(d):
                    return True
                graph[cur].insert(i,d)
                res.pop()
            return False
        dfs("JFK")
        return res