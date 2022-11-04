class Solution:
    def reverseVowels(self, s: str) -> str:
        is_vowel = lambda ch: ch in 'aeiouAEIOU'
        
        rev_s_vowels = filter(is_vowel, reversed(s))
        return ''.join(next(rev_s_vowels) if is_vowel(ch) else ch for ch in s)
