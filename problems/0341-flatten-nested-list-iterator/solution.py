# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nested_list: list[NestedInteger]):
        self.xs = flatten(nested_list)
        self.next_x = None
    
    def next(self) -> int:
        self.hasNext()
        x, self.next_x = self.next_x, None
        return x
    
    def hasNext(self) -> bool:
        self.next_x = next(self.xs, None) if self.next_x is None else self.next_x
        return self.next_x != None
    
def flatten(n_ints: list[NestedInteger]):
    yield from chain.from_iterable((x.getInteger(),) if x.isInteger() else flatten(x.getList()) for x in n_ints)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
