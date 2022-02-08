class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Knuth – Morris – Pratt (KMP)
        NOT_FOUND = -1

        def build_dfa(pattern: str):
            m = len(pattern)
            transitions = [defaultdict(int) for _ in range(m + 1)]

            i, j = -1, 0
            while j < m:
                ch = pattern[j]

                transitions[j] |= transitions[i]
                transitions[j][ch] = j + 1

                i = transitions[i][ch]
                j = transitions[j][ch]

            transitions.pop()  # Remove dummy -1 index used for i, j = -1, 0 case
            return transitions

        def search(pattern_dfa: dict, text: str) -> int:
            state, end_state = 0, len(pattern_dfa)

            for i, ch in enumerate(text):
                state = pattern_dfa[state][ch]
                if state == end_state:
                    return i - end_state + 1

            return NOT_FOUND

        dfa = build_dfa(needle)
        return search(dfa, haystack) if dfa else 0

