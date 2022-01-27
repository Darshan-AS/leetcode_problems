class Solution:
    @cache
    def superEggDrop(self, k: int, n: int) -> int:
        # (n, r) + (n, r - 1) + (n, r - 2) + .... + (n, 3) + (n, 2) + (n, 1)
        def comb_sum(n: int, r: int) -> int:
            return sum(islice(accumulate(
                range(1, r + 1),
                lambda a, x: a * (n - (x - 1)) // x,
                initial=1,
            ), 1, None))
        
        low, high = 1, n
        while low < high:
            moves = mid = (low + high) // 2
            max_n = comb_sum(moves, k)
            
            if max_n < n:
                low = mid + 1
            elif max_n > n:
                high = mid
            else:
                low = high = mid
        
        return low
