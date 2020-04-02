class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.find_next(n)
        return n == 1
    
    def find_next(self, n):
        next_n = 0
        while n:
            n, r = divmod(n, 10)
            next_n += r * r
        return next_n
