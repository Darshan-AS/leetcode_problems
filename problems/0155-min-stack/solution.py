class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        item = (x, min(x, self.getMin())) if self.stack else (x, x)
        self.stack.append(item)

    def pop(self) -> None:
        return self.stack.pop()[0] if self.stack else None

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
