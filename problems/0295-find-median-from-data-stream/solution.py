class MedianFinder:

    def __init__(self):
        self.smalls = [] # Max heap of small half
        self.larges = [] # Min heap of large half

    def addNum(self, num: int) -> None:
        if len(self.smalls) == len(self.larges):
            heappush(self.larges, -heappushpop(self.smalls, -num))
        else:
            heappush(self.smalls, -heappushpop(self.larges, num))

    def findMedian(self) -> float:
        return float((-self.smalls[0] + self.larges[0]) / 2 if len(self.smalls) == len(self.larges) else self.larges[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
