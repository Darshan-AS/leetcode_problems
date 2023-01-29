from dataclasses import dataclass


class DLLNode:

    def __init__(self, value=None, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next = next_


class LRUCache:
    @dataclass
    class Data:
        key: int
        value: int
        node: DLLNode

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, LRUCache.Data] = {}
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        d = self.cache[key]
        self.dll.remove(d.node)
        self.dll.append(d.node)

        return d.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            d = self.cache[key]
            self.dll.remove(d.node)
            self.cache.pop(d.key)

        if len(self.cache) == self.capacity:
            lru_key = self.dll.popleft().value
            self.cache.pop(lru_key)

        d = LRUCache.Data(key, value, DLLNode(key))
        self.dll.append(d.node)
        self.cache[key] = d


class DoublyLinkedList:

    def __init__(self):
        self.head, self.tail = DLLNode(), DLLNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def append(self, node: DLLNode) -> None:
        a, b, c = self.tail.prev, node, self.tail
        a.next, c.prev = b, b
        b.next, b.prev = c, a

    def appendleft(self, node: DLLNode) -> None: raise NotImplementedError()

    def pop(self) -> DLLNode: raise NotImplementedError()

    def popleft(self) -> DLLNode:
        node = self.head.next
        self.remove(node)
        return node

    def remove(self, node: DLLNode) -> None:
        a, b, c = node.prev, node, node.next
        a.next, c.prev = c, a
        b.next, b.prev = None, None

    def __bool__(self) -> bool:
        return self.head.next != self.tail

    def __iter__(self): raise NotImplementedError()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

