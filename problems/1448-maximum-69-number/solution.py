class Solution:
    def maximum69Number (self, num: int) -> int:
        i, k = 0, -1
        n = num
        while n:
            if n % 9 == 6: k = i
            n //= 10
            i += 1
        return num + 3 * 10 ** k if k != -1 else num
