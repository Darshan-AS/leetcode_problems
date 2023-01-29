from dataclasses import dataclass


class DLLNode:

    def __init__(self, value=None, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next = next_


class LFUCache:
    @dataclass
    class Data:
        key: int
        value: int
        freq: int
        node: DLLNode

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, LFUCache.Data] = {}
        self.freq_to_dll = defaultdict(DoublyLinkedList)
        self.min_freq = 1
        self.used = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        d = self.cache[key]
        self.freq_to_dll[d.freq].remove(d.node)
        self.freq_to_dll[d.freq + 1].append(d.node)
        self.cache[key] = LFUCache.Data(key, d.value, d.freq + 1, d.node)
        self.min_freq += self.min_freq == d.freq and not self.freq_to_dll[d.freq]

        return d.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return

        if key in self.cache:
            self.cache[key].value = value
            self.get(key)
            return

        if self.used == self.capacity:
            mf_dll = self.freq_to_dll[self.min_freq]
            mf_lru_key = mf_dll.popleft().value
            self.cache.pop(mf_lru_key)
            self.used -= 1

        d = LFUCache.Data(key, value, 1, DLLNode(key))
        self.freq_to_dll[d.freq].append(d.node)
        self.cache[key] = d
        self.used += 1
        self.min_freq = 1


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

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

