class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Boyer Moore
        NOT_FOUND = -1

        def build_skip_table(pattern: str) -> dict:
            return defaultdict(lambda: -1, {ch: i for i, ch in enumerate(pattern)})

        def search(pattern: str, skip_table: dict, text: str) -> int:
            m, n = len(pattern), len(text)
            i = 0

            while i <= n - m:
                j = m - 1

                while j >= 0 and text[i + j] == pattern[j]:
                    j -= 1

                if j < 0:
                    return i

                i += max(1, j - skip_table[text[i + j]])

            return NOT_FOUND

        st = build_skip_table(needle)
        return search(needle, st, haystack) if st else 0

