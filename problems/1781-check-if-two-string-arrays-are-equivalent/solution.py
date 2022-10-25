class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return all(starmap(
            operator.eq,
            zip_longest(
                chain.from_iterable(word1),
                chain.from_iterable(word2),
            ),
        ))
