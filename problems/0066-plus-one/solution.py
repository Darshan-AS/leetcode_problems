class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum, carry = 0, 1
        result = []
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + carry
            sum, carry = temp % 10, temp // 10
            result.append(sum)
        if carry:
            result.append(1)
        return result[::-1]
