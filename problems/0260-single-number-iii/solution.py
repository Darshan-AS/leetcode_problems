class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a_xor_b = reduce(xor, nums)
        fst_diff = a_xor_b & (~(a_xor_b - 1))
        split_a_b = lambda a, n: (a[0] ^ n, a[1]) if n & fst_diff else (a[0], a[1] ^ n)
        return reduce(split_a_b, nums, (0, 0))

