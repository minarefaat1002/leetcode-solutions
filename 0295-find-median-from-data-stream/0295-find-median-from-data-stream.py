class MedianFinder:

    def __init__(self):
        self.firstHalf = [] # maxHeap
        self.secondHalf = [] # minHeap

    def addNum(self, num: int) -> None:
        if len(self.firstHalf) > len(self.secondHalf):
            if self.firstHalf and -self.firstHalf[0] > num:
                heapq.heappush(self.secondHalf,-heapq.heappop(self.firstHalf))
                heapq.heappush(self.firstHalf,-num)
            else:
                heapq.heappush(self.secondHalf,num)
        else:
            if self.secondHalf and num > self.secondHalf[0]:
                heapq.heappush(self.firstHalf,-heapq.heappop(self.secondHalf))
                heapq.heappush(self.secondHalf,num)
            else:
                heapq.heappush(self.firstHalf,-num)
    def findMedian(self) -> float:
        if (len(self.firstHalf) + len(self.secondHalf)) % 2 == 0:
            return (-self.firstHalf[0] + self.secondHalf[0])/2
        else:
            return -self.firstHalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()