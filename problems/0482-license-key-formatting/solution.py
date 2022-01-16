from textwrap import wrap

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        return '-'.join(wrap(''.join(map(str.upper, filter(lambda ch: ch != '-', reversed(s)))), k))[::-1]
