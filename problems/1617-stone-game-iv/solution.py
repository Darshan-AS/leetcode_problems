class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = lambda x: (i * i for i in range(isqrt(x), 0, -1))
        next_wins = lambda a, x: setitem(a, x, not all(a[x - s] for s in squares(x))) or a
        return reduce(next_wins, range(n + 1), [False] * (n + 1))[-1]
