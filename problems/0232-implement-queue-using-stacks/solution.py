class MyQueue:

    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        self.front_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.back_stack.pop()

    def peek(self) -> int:
        if not self.back_stack:
            self.__flip_front_to_back()
        
        return self.back_stack[-1]

    def empty(self) -> bool:
        return not (self.front_stack or self.back_stack)
    
    def __flip_front_to_back(self) -> None:
        while self.front_stack:
            self.back_stack.append(self.front_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
