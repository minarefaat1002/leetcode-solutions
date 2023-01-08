class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        freeServers = [[server,i] for i,server in enumerate(servers)]
        heapq.heapify(freeServers)
        runningServers = []
        heapq.heapify(runningServers)
        for i,task in enumerate(tasks):
            while runningServers and i>= runningServers[0][0]:
                heapq.heappush(freeServers,heapq.heappop(runningServers)[1:])
            if freeServers:
                start = i
                minFreeServer = heapq.heappop(freeServers)
                res.append(minFreeServer[1])
                heapq.heappush(runningServers, [start+task] + minFreeServer )
            else:
                minFreeServer = heapq.heappop(runningServers)
                res.append(minFreeServer[2])
                start = max(minFreeServer[0],i)
                minFreeServer[0] = start + task
                heapq.heappush(runningServers,minFreeServer)
        return res