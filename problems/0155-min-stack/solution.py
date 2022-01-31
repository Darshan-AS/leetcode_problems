class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
