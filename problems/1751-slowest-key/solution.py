class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max(zip(map(lambda x: x[0] - x[1], zip(releaseTimes, [0] + releaseTimes)), keysPressed))[1]
