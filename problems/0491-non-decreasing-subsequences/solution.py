class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        masks = (map(int, reversed(bin(m)[2:])) for m in range(2 ** len(nums)))
        all_sub_seqns = (tuple(compress(nums, m)) for m in masks)

        is_non_decr = lambda xs: all(starmap(le, pairwise(xs)))
        is_len_ge_2 = lambda xs: len(xs) >= 2

        return set(s for s in all_sub_seqns if is_non_decr(s) and is_len_ge_2(s))

        
