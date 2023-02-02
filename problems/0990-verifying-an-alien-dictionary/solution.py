class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        EMPTY = ""
        ordinals = {ch: i for i, ch in enumerate(chain((EMPTY,), order))}

        def is_lexico(s1: str, s2: str) -> bool:
            pairs = zip_longest(s1, s2, fillvalue=EMPTY)
            a, b = next(dropwhile(lambda ab: eq(*ab), pairs), (EMPTY, "z"))
            return ordinals[a] < ordinals[b]
        
        return all(starmap(is_lexico, pairwise(words)))
        
