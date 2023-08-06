class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        num_lists = [[0] * (n + 1) for _ in range(goal + 1)]
        num_lists[0][0] = 1
        for i, j in product(range(1, goal + 1), range(1, n + 1)):
            num_lists[i][j] = (num_lists[i - 1][j - 1] * (n - j + 1) + num_lists[i - 1][j] * max(j - k, 0)) % 1_000_000_007
        return num_lists[-1][-1]

