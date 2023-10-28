class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1_000_000_007
        dfa = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}

        return sum(reduce(
            lambda a, _: {ch: sum(a[x] for x in dfa[ch]) % M for ch in dfa.keys()},
            range(1, n),
            dict(zip(dfa.keys(), repeat(1))),
        ).values()) % M
        
