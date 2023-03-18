from dataclasses import dataclass

class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = DLLNode(homepage)

    def visit(self, url: str) -> None:
        a, b = self.page, DLLNode(url)
        a.next, b.prev = b, a
        self.page = b

    def back(self, steps: int) -> str:
        while self.page.prev and steps: self.page = self.page.prev; steps -= 1
        return self.page.value

    def forward(self, steps: int) -> str:
        while self.page.next and steps: self.page = self.page.next; steps -= 1
        return self.page.value

@dataclass
class DLLNode:
    value: Any = None
    prev: 'DLLNode | None' = None
    next: 'DLLNode | None' = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
