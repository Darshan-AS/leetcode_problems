class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        q = deque()
        q.append(x)
        q.append(self.queue)
        self.queue = q

    def pop(self) -> int:
        assert not self.empty()
        
        value = self.queue.popleft()
        self.queue = self.queue.popleft()
        return value

    def top(self) -> int:
        assert not self.empty()
        
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
