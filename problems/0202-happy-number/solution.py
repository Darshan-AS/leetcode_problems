class Solution(object):
    def find_next(self, i):
        next_i = 0
        while i > 0:
            next_i += (i % 10)**2
            i = i // 10
        return next_i
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = n
        seen = set()
        while i not in seen:
            if i == 1:
                return True
            seen.add(i)
            i = self.find_next(i)
        return False
            
            
