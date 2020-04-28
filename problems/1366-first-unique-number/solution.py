class Node:
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cache = {}
        self.head = self.tail = Node(-1)
        
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        return self.head.next.value if self.head.next else self.head.value

    def add(self, value: int) -> None:
        if value not in self.cache:
            node = Node(value)
            self.insert_at_tail(node)
            self.cache[value] = node
            return
        
        node = self.cache[value]
        if node:
            self.remove_node(node)
            self.cache[value] = None
        
    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        
        if not next_node:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            return
        
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None
        
    def insert_at_tail(self, node):        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
