class Solution:
    def addDigits(self, num: int) -> int:
        return mod(num, 9) or min(num, 9)
