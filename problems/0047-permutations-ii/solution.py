class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def permutations(a: list, r: int = None) -> iter:
            r = len(a) if r is None else r

            yield from (
                [x] + p
                for x, i in dict(map(reversed, reversed(list(enumerate(a))))).items()
                for p in permutations(a[:i] + a[i + 1:], r - 1)
            ) if a and r else ([],)
        
        return list(permutations(nums))
