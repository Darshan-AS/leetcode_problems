class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        T = TypeVar('T')
        def triplewise(xs: Iterable[T]) -> Iterator[tuple[T, T, T]]:
            a, b, c = tee(xs, 3)
            next(b, None); next(c, None); next(c, None)
            return zip(a, b, c)
        
        w = {'A': 1, 'B': -1}
        count = lambda a, b, c: (a == b == c) * w[a]
        
        return sum(starmap(count, triplewise(colors))) > 0
        
