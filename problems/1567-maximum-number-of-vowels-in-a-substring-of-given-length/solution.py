class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return max(accumulate(
            zip(chain(repeat('z', k), s), s),
            lambda a, x: a - (x[0] in 'aeiou') + (x[1] in 'aeiou'),
            initial=0,
        ))
