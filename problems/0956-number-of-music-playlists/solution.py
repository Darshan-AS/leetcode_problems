class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        num_lists = [0] * (n + 1)
        num_lists[0] = prev = 1
        for i, j in product(range(1, goal + 1), range(1, n + 1)):
            prev, num_lists[j] = num_lists[j] * (j != n), (prev * (n - j + 1) + num_lists[j] * max(j - k, 0)) % 1_000_000_007
        return num_lists[-1]

