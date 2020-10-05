from math import ceil, log

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return ~n & ((1 << ceil(log(n, 2))) - 1) if n else 1
