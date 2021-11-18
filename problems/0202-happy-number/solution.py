class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(map(lambda num: num * num, map(int, str(n))))
        return n == 1
        
