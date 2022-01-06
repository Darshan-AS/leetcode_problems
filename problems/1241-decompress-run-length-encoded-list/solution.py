class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return list(chain.from_iterable(
            repeat(val, freq)
            for freq, val in zip(
                islice(nums, 0, None, 2),
                islice(nums, 1, None, 2),
            )
        ))
