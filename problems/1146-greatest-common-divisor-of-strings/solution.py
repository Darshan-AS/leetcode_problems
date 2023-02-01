class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        return s1[:gcd(len(s1), len(s2))] if all(map(eq, chain(s1, s2), chain(s2, s1))) else ""
