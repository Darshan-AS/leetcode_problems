class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        return max(accumulate(gain, add, initial=0))
