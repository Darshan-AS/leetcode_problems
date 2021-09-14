class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        reversed_alphas = filter(lambda x: x.isalpha(), reversed(s))
        return ''.join(ch if not ch.isalpha() else next(reversed_alphas) for ch in s)
