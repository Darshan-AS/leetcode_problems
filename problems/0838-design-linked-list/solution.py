class MyLinkedList:
    class Node:
        def __init__(self, value: Any = None, next_ = None) -> None:
            self.value = value
            self.next = next_

    def __init__(self):
        self.head = self.tail = MyLinkedList.Node()

    def get(self, index: int) -> int:
        node = self.head.next
        i = 0
        while node and i != index:
            node = node.next
            i += 1
        
        return node.value if node else -1

    def addAtHead(self, val: int) -> None:
        self.head.next = MyLinkedList.Node(val, self.head.next)
        if self.tail.next: self.tail = self.tail.next

    def addAtTail(self, val: int) -> None:
        self.tail.next = MyLinkedList.Node(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        i = 0
        while node and i != index:
            node = node.next
            i += 1
        
        if not node: return
        
        node.next = MyLinkedList.Node(val, node.next)
        if self.tail.next: self.tail = self.tail.next

    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        i = 0
        while node and i != index:
            node = node.next
            i += 1
        
        if not node or not node.next: return
        
        node.next = node.next.next
        if not node.next: self.tail = node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
