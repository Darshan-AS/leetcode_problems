class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        is_not_sorted = lambda xs: any(starmap(gt, pairwise(xs)))
        return sum(map(is_not_sorted, zip(*strs)))

