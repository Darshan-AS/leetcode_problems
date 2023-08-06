class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        M = MOD = 1_000_000_007

        facts  = tuple(accumulate(range(1, n + 1), lambda a, x: a * x % M, initial=1))
        ifacts = tuple((pow(x, M - 2, M) for x in facts)) # Fermat's little theorem

        terms = (pow(i - k, goal - k, M) * ifacts[n - i] * ifacts[i - k] % M for i in range(n, k - 1, -1))
        num_lists = facts[n] * sum(map(mul, terms, cycle((1, -1)))) % M

        return num_lists


