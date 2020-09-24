from functools import reduce

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return reduce(lambda x, y: chr(ord(x) ^ ord(y)), s + t)
