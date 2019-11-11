class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, i = 0, n
        while i > 0:
            if i % 2:
                count += 1
            i = i // 2
        
        return count
