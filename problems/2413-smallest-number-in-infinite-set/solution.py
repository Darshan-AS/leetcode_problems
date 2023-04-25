class SmallestInfiniteSet:

    def __init__(self):
        self.k: int = 1
        self.added: set[int] = set()
        self.added_hq: list[int] = []

    def popSmallest(self) -> int:
        if self.added_hq:
            num = heappop(self.added_hq)
            self.added.remove(num)
        else:
            num = self.k
            self.k += 1
        return num

    def addBack(self, num: int) -> None:
        if num >= self.k or num in self.added: return
        heappush(self.added_hq, num)
        self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
