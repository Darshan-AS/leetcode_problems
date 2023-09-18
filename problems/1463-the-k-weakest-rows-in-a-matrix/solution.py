class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]
        
