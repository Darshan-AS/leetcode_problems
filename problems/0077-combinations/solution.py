class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(iterable: iter, r: int):
            pool = tuple(iterable)
            n = len(pool)
            
            if r > n:
                return

            if r < 1 or not pool:
                yield ()
                return

            yield from combinations(pool[:-1], r)
            yield from (c + (pool[-1],) for c in combinations(pool[:-1], r - 1))
        
        return list(combinations(range(1, n + 1), k))
