class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        return nsmallest(k, range(len(mat)),
            key=tuple(bisect_right(row, -1, key=neg) for row in mat).__getitem__,
        )
