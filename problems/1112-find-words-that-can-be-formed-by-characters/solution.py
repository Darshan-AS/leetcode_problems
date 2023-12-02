class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        return (c := Counter(chars)) and sum(len(s) for s in words if Counter(s) <= c)
