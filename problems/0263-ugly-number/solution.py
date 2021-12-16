class Solution:
    def isUgly(self, num: int) -> bool:
        def repeated_divide(n, k):
            while n and n % k == 0:
                n = n // k
            return n
        
        num = repeated_divide(num, 2)
        num = repeated_divide(num, 3)
        num = repeated_divide(num, 5)
        return num == 1
