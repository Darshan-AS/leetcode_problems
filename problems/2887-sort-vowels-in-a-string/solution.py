class Solution:
    def sortVowels(self, s: str) -> str:
        is_vowel = tuple(x in 'AEIOUaeiou' for x in s)
        s_vowels = iter(sorted(compress(s, is_vowel)))
        return ''.join(next(s_vowels) if v else x for x, v in zip(s, is_vowel))
