class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        
        a = n // 5
        return a + self.trailingZeroes(a)
