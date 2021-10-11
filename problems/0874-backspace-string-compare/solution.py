from itertools import zip_longest

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_text_rev(text: str):
            backspace = 0
            for ch in reversed(text):
                if ch == '#':
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    yield ch
        
        return all(s_ch == t_ch for s_ch, t_ch in zip_longest(final_text_rev(s), final_text_rev(t)))
