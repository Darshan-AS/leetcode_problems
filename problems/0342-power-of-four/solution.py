import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and math.log(num, 4).is_integer()
