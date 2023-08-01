class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        T = TypeVar('T')
        def combinations(pool: Iterable[T], r: int = None) -> Iterator[Iterator[T]]:
            pool = tuple(pool)
            r = len(pool) if r is None else r

            yield from ((
                (x,) + p
                for i, x in enumerate(pool)
                for p in combinations(pool[i + 1:], r - 1)
            ) if pool else ()) if r else ((),)
        
        return list(combinations(range(1, n + 1), k))
