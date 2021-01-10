from itertools import chain, zip_longest

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(ch1 == ch2 for ch1, ch2 in zip_longest(chain(*word1), chain(*word2)))
