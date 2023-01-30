class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        q = deque()
        q.append([0,0])
        visited = set()
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if targetCapacity in [jug1Capacity,jug2Capacity,jug1Capacity+jug2Capacity]:
            return True
        while q:
            c1,c2 = q.popleft()
            if (c1,c2) in visited:
                continue
            if c1+c2 == targetCapacity:
                return True
            visited.add((c1,c2))
            q.append([jug1Capacity,c2])
            q.append([c1,jug2Capacity])
            q.append([jug1Capacity,jug2Capacity])
            q.append([0,c2])
            q.append([c1,0])
            q.append([c1+min(jug1Capacity-c1,c2),max(c2-(jug1Capacity-c1),0)])
            c1,c2 = c2,c1
            q.append([c1+min(jug1Capacity-c1,c2),max(c2-(jug1Capacity-c1),0)])
        return False