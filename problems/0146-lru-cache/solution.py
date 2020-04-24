class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.move_to_tail(self.cache[key])
        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.move_to_tail(self.cache[key])
            return
        
        if self.is_full():
            head_node = self.remove_from_head()
            del self.cache[head_node.key]
            self.size -= 1
            
        node = Node(key, value)
        self.cache[key] = node
        self.insert_at_tail(node)
        self.size += 1
        
    def move_to_tail(self, node):
        prev_node = node.prev
        next_node = node.next
        
        if not next_node:
            return
        
        if not prev_node:
            self.remove_from_head()
            self.insert_at_tail(node)
            return
        
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None
        self.insert_at_tail(node)
        
    def is_full(self):
        return self.size == self.capacity
        
    
    def remove_from_head(self):
        if not self.head:
            return
        
        node = self.head
        self.head = node.next
        
        if not self.head:
            self.tail = self.head
        else:
            self.head.prev.next = None
            self.head.prev = None
        
        return node
        
    
    def insert_at_tail(self, node):
        if not self.tail:
            self.head = self.tail = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
