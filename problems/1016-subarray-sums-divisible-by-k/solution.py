class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        return sum(map(
            lambda n: n * (n - 1) // 2,
            Counter(accumulate(nums, lambda a, x: (a + x % k) % k, initial=0)).values(),
        ))
