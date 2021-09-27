from itertools import chain

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def letter_case_permutation(i: int = 0):
            if i >= len(s):
                yield ()
                return
            
            ch = s[i]
            if ch.isalpha():
                yield from (chain(ch.lower(), p) for p in letter_case_permutation(i + 1))
                yield from (chain(ch.upper(), p) for p in letter_case_permutation(i + 1))
            else:
                yield from (chain(ch, p) for p in letter_case_permutation(i + 1))
                
        return list(map(lambda x: ''.join(x), letter_case_permutation()))
