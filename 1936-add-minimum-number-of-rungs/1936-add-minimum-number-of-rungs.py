class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        addedRungs = 0
        rungs = [0] + rungs
        for i in range(1,len(rungs)):
            addedRungs += (rungs[i]-rungs[i-1]-1)//dist
        return addedRungs