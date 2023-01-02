class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all(map(str.isupper, word)) or all(map(str.islower, islice(word, 1, None)))
