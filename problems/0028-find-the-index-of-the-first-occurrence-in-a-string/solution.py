class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Rabin Karp
        NOT_FOUND = -1

        R, Q = 256, 1_000_000_007
        RM = pow(R, len(needle) - 1, Q)

        def build_hash(pattern: str) -> int:
            return reduce(lambda a, x: (a * R + x) % Q, map(ord, pattern), 0)

        def search(pattern_hash: int, pattern_len: int, text: str) -> int:
            m, n = pattern_len, len(text)
            h = 0

            for i in range(n):
                h = (h + Q - RM * ord(text[i - m]) % Q) % Q if i >= m else h
                h = (h * R + ord(text[i])) % Q
                if i >= m - 1 and h == pattern_hash:
                    return i - m + 1

            return NOT_FOUND

        hash_ = build_hash(needle)
        return search(hash_, len(needle), haystack) if hash_ else 0

