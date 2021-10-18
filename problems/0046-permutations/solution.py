class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(iterable: iter, r: int = None):
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r

            if r > n:
                return

            if r < 1 or not pool:
                yield ()
                return

            yield from permutations(pool[:-1], r)
            yield from (
                p[:i] + (pool[-1],) + p[i:]
                for p in permutations(pool[:-1], r - 1)
                for i in range(len(p), -1, -1)
            )
            
            # for i, x in enumerate(pool):
            #     yield from ((x,) + p for p in permutations(pool[:i] + pool[i + 1 :], r - 1))
        
        return list(permutations(nums))
