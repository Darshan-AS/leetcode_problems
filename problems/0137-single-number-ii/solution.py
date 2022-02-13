class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def counts(a, num):
            _1s, _2s = a
            _1s = (_1s ^ num) & ~_2s
            _2s = (_2s ^ num) & ~_1s
            return _1s, _2s
        
        return reduce(counts, nums, (0, 0))[0]
