class Solution:
    def maxScore(self, s: str) -> int:
        return max(islice(accumulate(s, lambda a, x: a + (x == '0') - (x == '1'), initial=s.count('1')), 1, len(s)))
        
