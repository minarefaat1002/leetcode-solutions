class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        seen = set()
        q.append(0)
        seen.add(0)
        while q:
            popped = q.popleft()
            for key in rooms[popped]:
                if key not in seen:
                    seen.add(key)
                    q.append(key)
        return len(seen) == len(rooms)