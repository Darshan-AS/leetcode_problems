class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def counts(a, num):
            _1s, _2s, _3s = a
            _2s_and_3s = _2s | (_1s & num)
            _1s_and_3s = _1s ^ num
            _3s = _1s_and_3s & _2s_and_3s
            _1s = _1s_and_3s & (~_3s)
            _2s = _2s_and_3s & (~_3s)
            return _1s, _2s, _3s
            
        return reduce(counts, nums, (0, 0, 0))[0]
