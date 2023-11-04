class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        return max(chain(left, map(sub, repeat(n), right)))
        
