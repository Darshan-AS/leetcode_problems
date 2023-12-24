class Solution:
    def minOperations(self, s: str) -> int:
        return min(x := sum(map(ne, s, cycle('01'))), len(s) - x)
