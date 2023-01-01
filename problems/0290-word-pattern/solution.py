class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return len(set(pattern)) == len(set(words)) == len(set(zip_longest(pattern, words)))
