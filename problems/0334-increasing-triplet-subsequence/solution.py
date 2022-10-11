from numbers import Number

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        def increasing_k(seq: list[Number], k: int) -> bool:
            mins = [math.inf] * (k - 1)
            for v in seq:
                i = bisect.bisect_left(mins, v)
                if i == k - 1: return True
                mins[i] = v
            return False
        
        return increasing_k(nums, 3)
