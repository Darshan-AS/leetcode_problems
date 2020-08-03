class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.state = 0 

    def add(self, key: int) -> None:
        self.state |= (1 << key)

    def remove(self, key: int) -> None:
        self.state &= ~(1 << key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.state & 1 << key

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
