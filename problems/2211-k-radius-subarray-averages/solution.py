class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        w = 2 * k + 1
        if len(nums) < w: return [-1] * len(nums)

        lefts, rights = iter(nums), iter(nums)
        first_sum = sum(islice(rights, w))

        sums = accumulate(zip(lefts, rights), lambda a, x: a + x[1] - x[0], initial=first_sum)
        return list(chain(repeat(-1, k), (s // w for s in sums), repeat(-1, k)))
