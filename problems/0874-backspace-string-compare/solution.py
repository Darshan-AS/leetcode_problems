from itertools import zip_longest
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def correct_string(s):
            backspace_count = 0
            for x in reversed(s):
                if x == '#': backspace_count += 1
                elif backspace_count: backspace_count -= 1
                else: yield x
        
        return all(x == y for x, y in zip_longest(correct_string(S), correct_string(T)))
