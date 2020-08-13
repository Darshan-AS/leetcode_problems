from functools import reduce

class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha_to_int_map = dict(zip(string.ascii_uppercase, range(1, 27)))
        return reduce(lambda ans, ch: ans * 26 + alpha_to_int_map[ch], s, 0)
