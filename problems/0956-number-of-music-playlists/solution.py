class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def num_lists(i: int, j: int) -> int:
            if not i and not j: return 1
            if not i  or not j: return 0
            return (num_lists(i - 1, j - 1) * (n - j + 1) + num_lists(i - 1, j) * max(j - k, 0)) % 1_000_000_007
        
        return num_lists(goal, n)

