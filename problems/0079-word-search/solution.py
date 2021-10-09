class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)

        seen = set()

        # Refactored due to TLE on prev solution. Time complexity remains same
        def dfs_exists(i: int, j: int, k: int) -> bool:
            if k + 1 >= w:
                return True

            seen.add((i, j))
            exists = any(
                dfs_exists(i + di, j + dj, k + 1)
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
                if 0 <= i + di < m
                and 0 <= j + dj < n
                and (i + di, j + dj) not in seen
                and board[i + di][j + dj] == word[k + 1]
            )
            seen.remove((i, j))

            return exists

        return any(
            dfs_exists(x, y, 0)
            for x, y in itertools.product(range(m), range(n))
            if board[x][y] == word[0]
        )

