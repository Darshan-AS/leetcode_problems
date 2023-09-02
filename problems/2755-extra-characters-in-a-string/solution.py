class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        words = set(dictionary)
        
        extras = list(range(len(s) + 1))
        for j in range(1, len(s) + 1):
            extras[j] = min(extras[i] if s[i:j] in words else extras[j - 1] + 1 for i in range(j))
        return extras[-1]
