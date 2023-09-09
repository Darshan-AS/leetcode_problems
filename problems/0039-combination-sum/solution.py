class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def comb_sum(i: int, k: int) -> Iterator[list]:
            yield from chain(
                comb_sum(i - 1, k),
                (c.append(candidates[i]) or c for c in comb_sum(i, k - candidates[i])),
            ) if i >= 0 and k > 0 else () if k else ([],)
        
        return list(comb_sum(len(candidates) - 1, target))
        
