class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes_count = 0
        while n:
            zeroes_count += n // 5
            n = n // 5
        
        return zeroes_count
