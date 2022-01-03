class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(pool: list, r: int, index: int=0):
            if r == 0:
                yield ()
                return
            
            if not (0 < r <= len(pool) and 0 <= index < len(pool)):
                return

            yield from (chain((pool[index],), c) for c in combinations(pool, r - 1, index + 1))
            yield from combinations(pool, r, index + 1)
        
        return list(map(list, combinations(list(range(1, n + 1)), k)))
