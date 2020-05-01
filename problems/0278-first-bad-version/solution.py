# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        
        if isBadVersion(i):
            return i
        else:
            i += 1
        
        while i <= j:
            m = (i + j) // 2
            
            if not isBadVersion(m):
                i = m + 1
                continue
            
            if not isBadVersion(m - 1):
                return m
            else:
                j = m - 1
        
        return n
