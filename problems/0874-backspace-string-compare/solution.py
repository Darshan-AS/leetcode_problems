class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_text_rev(text: str) -> str:
            backspace = 0
            for ch in reversed(text):
                if ch == '#': backspace += 1
                elif backspace: backspace -= 1
                else: yield ch
        
        return all(starmap(eq, zip_longest(final_text_rev(s), final_text_rev(t))))
