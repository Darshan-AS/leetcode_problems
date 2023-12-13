class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        return sum(
            sum(row[col] for row in mat) == 1
            for col in (row.index(1) for row in mat if sum(row) == 1)
        )
