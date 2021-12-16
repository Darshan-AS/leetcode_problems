class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(map(int, str(num)))
        return num
