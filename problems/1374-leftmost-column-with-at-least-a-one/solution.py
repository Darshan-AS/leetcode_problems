# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, b: 'BinaryMatrix') -> int:
        n, m = b.dimensions()
        
        i, j = 0, m - 1
        while i < n and j >= 0:
            if b.get(i, j):
                j -= 1
            else:
                i += 1
        
        return -1 if j == m - 1 else j + 1
