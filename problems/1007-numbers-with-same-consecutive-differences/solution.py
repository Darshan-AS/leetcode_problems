class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def helper(num, n):
            if not n:
                yield num
                return
            
            last_digit = num % 10
            next_digits = set((last_digit + K, last_digit - K))
            
            for j in next_digits:
                if 0 <= j <= 9:
                    yield from helper(num * 10 + j, n - 1)
        
        begin = 0 if N == 1 else 1
        return list(chain(*(helper(i, N - 1) for i in range(begin, 10))))
