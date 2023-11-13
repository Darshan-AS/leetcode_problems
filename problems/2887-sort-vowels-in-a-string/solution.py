class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        c = Counter(s)
        s_vowels = chain.from_iterable(repeat(v, c[v]) for v in vowels)
        return ''.join(next(s_vowels) if x in vowels else x for x in s)
