class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) +1)%10)
                res.append( lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) -1+10)%10)
                res.append( lock[:i] + digit + lock[i+1:])
            return res
                
        q = deque()
        q.append(["0000",0]) #[loack , turns]
        visit = set(deadends)
        #we can make a set for the deadends but for the sake of simplicity we will append them as visited in the set visit 
        while q:
            lock , turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child,turns+1])
        return -1