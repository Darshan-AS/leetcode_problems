# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        def iterLL(head: ListNode) -> Iterator[Any]:
            while head:
                yield head.val
                head = head.next
        
        r_val = math.inf
        for i, val in enumerate(iterLL(self.head)):
            j = random.randint(0, i)
            if j == 0: r_val = val
        
        return r_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
