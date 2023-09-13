class Solution:
    def candy(self, ratings: list[int]) -> int:
        share = lambda xs: accumulate(starmap(lt, pairwise(xs)), lambda a, x: a * x + 1, initial=1)
        return sum(map(max, share(ratings), reversed(list(share(reversed(ratings))))))
