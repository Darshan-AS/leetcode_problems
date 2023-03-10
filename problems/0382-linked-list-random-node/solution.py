# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode | None):
        self.head = head

    def getRandom(self) -> int:
        return reduce(
            lambda a, x: x[1].val if randint(0, x[0]) == 0 else a,
            enumerate(iter_LL(self.head)),
            None,
        )
    
def iter_LL(ll: ListNode | None) -> Iterable[ListNode]:
    while ll: yield ll; ll = ll.next


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
