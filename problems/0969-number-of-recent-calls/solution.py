from collections import deque
from bisect import bisect

class RecentCounter:
    TIME_FRAME = 3000
    
    def __init__(self):
        self.history = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.history.append(t)
        return len(self.history) - bisect_left(self.history, t - self.TIME_FRAME, self.start)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
