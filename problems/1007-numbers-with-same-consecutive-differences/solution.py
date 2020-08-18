class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def helper(num, n):
            if not n:
                yield num
                return
            
            last_digit = num % 10
            a, b = last_digit + K, last_digit - K
            
            for j in set((a, b)):
                if 0 <= j <= 9:
                    yield from helper(num * 10 + j, n - 1)
        
        ans = []
        for i in range(0 if N == 1 else 1, 10):
            ans.extend(list(helper(i, N - 1)))
        return ans
