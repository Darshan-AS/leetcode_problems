class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, i = 0, n
        while i > 0:
            count += 1
            i = i & (i - 1)
        
        return count
