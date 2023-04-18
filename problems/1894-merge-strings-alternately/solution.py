class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(chain.from_iterable(zip_longest(word1, word2, fillvalue='')))
