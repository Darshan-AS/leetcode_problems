class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.k_largest = nums.copy()
        
        heapify(self.k_largest)
        while len(self.k_largest) > self.k: heappop(self.k_largest)

    def add(self, val: int) -> int:
        heappush(self.k_largest, val)
        if len(self.k_largest) > self.k: heappop(self.k_largest)
        return self.k_largest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
