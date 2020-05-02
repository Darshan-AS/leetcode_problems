class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return sum(i in jewels for i in S)
