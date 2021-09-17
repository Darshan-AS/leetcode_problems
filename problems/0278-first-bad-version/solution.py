# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n
        
        while low < high:
            mid = (low + high) // 2
            low, high = (low, mid) if isBadVersion(mid) else (mid + 1, high)
        
        return low
        
