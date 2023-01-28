from sortedcontainers import SortedDict
class SummaryRanges:

    def __init__(self):
        self.sd = SortedDict()

    def addNum(self, value: int) -> None:
        self.sd[value] = value

    def getIntervals(self) -> List[List[int]]:
        res = []
        for key in self.sd:
            if res and key-1 == res[-1][1]:
                res[-1][1] += 1
            else:
                res.append([key,key])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()