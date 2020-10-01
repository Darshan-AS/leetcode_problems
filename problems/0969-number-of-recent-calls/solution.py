from collections import deque

class RecentCounter:
    TIME_FRAME = 3000
    
    def __init__(self):
        self.history = deque()

    def ping(self, t: int) -> int:
        self.history.append(t)
        while self.history[0] < t - RecentCounter.TIME_FRAME:
            self.history.popleft()
        return len(self.history)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
