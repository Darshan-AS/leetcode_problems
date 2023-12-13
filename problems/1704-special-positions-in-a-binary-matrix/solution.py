class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        special_rows = (row for row in mat if sum(row) == 1)
        maybe_special_cols = (row.index(1) for row in special_rows)
        special_cols = (col for col in maybe_special_cols if sum(row[col] for row in mat) == 1)
        return sum(1 for _ in special_cols)
