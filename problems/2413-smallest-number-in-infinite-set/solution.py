from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.k = 1
        self.added = SortedSet()

    def popSmallest(self) -> int:
        if self.added: return self.added.pop(0)
        else: self.k += 1; return self.k - 1

    def addBack(self, num: int) -> None:
        if num < self.k: self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
