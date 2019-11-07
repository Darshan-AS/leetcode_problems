class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes_count = 0
        i = n
        while i:
            i = i // 5
            zeroes_count += i
        
        return zeroes_count
