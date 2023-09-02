class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        words = set(dictionary)

        @cache
        def extras(j: int) -> int:
            return j and min(extras(i) if s[i:j] in words else extras(j - 1) + 1 for i in range(j))
        
        return extras(len(s))
        
