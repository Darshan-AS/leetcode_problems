class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(a: list, r: int = None) -> iter:
            r = len(a) if r is None else r

            yield from (
                [x] + p
                for i, x in enumerate(a)
                for p in permutations(a[:i] + a[i + 1:], r - 1)
            ) if a and r else ([],)
        
        return list(permutations(nums))
